from sqlalchemy import create_engine
import pandas as pd 
import numpy as np 
host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_loja'
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

#Leitura dos dados da tabela de produtos
df_estoque = pd.read_sql('tb_produtos', engine)

#printando somente os 5 primeiros
print(df_estoque.head())

#Calcula o valor do estoque por linha
df_estoque['TotalEstoque'] = df_estoque['QuantidadeEstoque'] * df_estoque['Valor']
print(df_estoque[['NomeProduto','TotalEstoque']])

#agrupando produto com mesmo nome e somando as quantidades e valores
df_soma = df_estoque.groupby('NomeProduto').agg({
    'QuantidadeEstoque':'sum',
    'TotalEstoque': 'sum'
    })#.reset_index()
print(f'{df_soma} atualizado!!!')

#ordenando os produtos pelo total de estoque
df_ordenado = df_estoque.sort_values(by='TotalEstoque', ascending= False)
print(df_ordenado[['NomeProduto','TotalEstoque']])


#Calcula o valor total do estoque
print(f'Total geral em estoque: R${df_estoque["TotalEstoque"].sum()}')

# mediana = np.median(df_estoque['TotalEstoque'])
# print(f'Essa é o valor chave do estoque {mediana}')

# media = np.mean(df_estoque['TotalEstoque'])
# print(f'Essa é a media {media}')

# transformando o campo total estoque em um array numpy
# array_total_estoque = np.array(df_estoque['TotalEstoque'])

# #print array_total_estoque
# media = np.mean(array_total_estoque)
# mediana = np.median(array_total_estoque)

# print(f'Essa é a media do estoque {media:.2f}')
# print(f'Essa é a mediana do estoque {mediana:.2f}')
# # distancia = (media - mediana)/mediana
# # print(distancia)
# distancia = abs((media - mediana)/mediana) * 100
# print(f'{distancia:.2f}')
# q1 = np.quantile(array_total_estoque, 0.25)
# q2 = np.quantile(array_total_estoque, 0.50)
# q3 = np.quantile(array_total_estoque, 0.75)