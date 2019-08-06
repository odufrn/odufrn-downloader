# Open Data UFRN Downloader
[![PyPI version](https://badge.fury.io/py/odufrn-downloader.svg)](https://badge.fury.io/py/odufrn-downloader)

Pacote para baixar os dados do portal de [dados abertos da UFRN](dados.ufrn.br).

```bash
pip install odufrn-downloader
```

## Utilizando

```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Lista os conjuntos de dados
ufrn_data.list_datasets()

# Baixa um conjunto de dados
ufrn_data.download_dataset('discentes')

# Baixa uma lista de conjuntos de dados
datasets = ['discentes', 'dados-complementares-de-discentes', 'dados-socio-economicos-de-discentes']
ufrn_data.download_datasets(datasets)
```

----------------
Projeto idealizado por [Ítalo Epifânio](https://github.com/itepifanio).
Link do projeto original [aqui](https://github.com/professorCheatSheet/dadosAbertosUFRNDownloader).
