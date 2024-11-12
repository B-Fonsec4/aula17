import pandas as pd
import numpy as np 
try:
    print('Obtendo dados...')
    ENDERECO_DADOS ='https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv'
    #Encondings: utf-8 iso-8859-1, latin1, cp1252
    df_ocorrencias = pd.read_csv(ENDERECO_DADOS, sep=';', encoding='iso-8859-1')
    df_estel_mes = df_ocorrencias[['mes','estelionato']]
    df_estel_mes = df_estel_mes.groupby(['mes']).sum(['estelionato'])
    print(df_estel_mes.head())


except Exception as e:
    print(f' ERRO {e}')
    exit()

try:
        # somando o total de estelionatos
    df_total_estelionato = df_estel_mes['estelionato'].sum()
    # print(df_total_estelionato)
    media_estelionato = np.mean(df_total_estelionato)
    mediana_estelionato = np.median(df_total_estelionato)
    distancia = abs((media_estelionato - mediana_estelionato)/mediana_estelionato)
    print(f'essa é a media {media_estelionato}')
    print(f'essa é a mediana {mediana_estelionato}')
    print(f'Temos em media {media_estelionato} casos de estelionato no estado.')
except Exception as e:
    print(f' ERRO {e}')
    exit()