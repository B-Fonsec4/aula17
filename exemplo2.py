import pandas as pd 
import numpy as np

#obter dados
try:
    print('Obtendo dados...')
    ENDERECO_DADOS ='https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    #Encondings: utf-8 iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    #delimitando somente as variavei do Exemplo1: munic,roubo_veiculo
    df_roubo_veiculo = df_ocorrencias[['munic', 'roubo_veiculo']]
    df_roubo_veiculo = df_roubo_veiculo.groupby(['munic']).sum(['roubo_veiculo']).reset_index()
    print(df_roubo_veiculo.head())
except Exception as e:
    print(f'Erro ao obter dados: {e}')
    exit()

try:
    print('\n Calculando informações sobre padrão de roubo de veiculos...')
    array_roubo_veiculo = np.array(df_roubo_veiculo['roubo_veiculo'])
    # print(array_roubo_veiculo)
    media_roubo_veiculo = np.mean(array_roubo_veiculo)
    mediana_roubo_veiculo = np.median(array_roubo_veiculo)

    distancia = abs((media_roubo_veiculo - mediana_roubo_veiculo) / mediana_roubo_veiculo)
    print(f'{distancia:.2f}')
    print(f'A media de roubo de veiculos é {media_roubo_veiculo}')
    print(f'A mediana de roubo de veiculos é {mediana_roubo_veiculo}')


except Exception as e:
    print(f'Erro ao obter as informações sobre padrão de roubo de veiculos: {e}')
    exit()