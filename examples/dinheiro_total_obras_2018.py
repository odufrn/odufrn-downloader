# coding: utf-8
'''
Objetivo: Nesse script em questão queremos
descobrir a quantidade de dinheiro gasto
em licitações de obras em 2018 pela Universidade
Federal do Rio Grande do Norte (UFRN).

Requisitos: Pandas, ODUFRNDownloader

Use o comando a seguir para instalar as dependências
pip install pandas odufrn-downloader
'''

import pandas as pd
from odufrn_downloader import ODUFRNDownloader

ufrn_data = ODUFRNDownloader()
# Efetuando o download dos dados utilizando o ODUFRNDowloader
ufrn_data.download_package('obras', dictionary=False)

# Utilizando o pandas para transformar o conjunto de dados em um DataFrame
obras = pd.read_csv('obras/Obras.csv', error_bad_lines=False, sep=';')

obras_2018 = obras[obras['licitacao'].str.contains('2018')]['valor']
# Removendo R$ e espaços dos dados selecionados
obras_2018 = obras_2018.str.replace('R', '').str.replace('$', '').str.strip()
# Substituindo vígula por ponto para converter para float
obras_2018 = obras_2018.str.replace('.', '').str.replace(',', '.')
# Transformando os dados de string para float
obras_2018 = obras_2018.astype(float)
print('O gasto da UFRN para obras em 2018 foi: R$ %.2f' % obras_2018.sum())
