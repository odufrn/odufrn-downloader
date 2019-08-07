# Open Data UFRN Downloader
[![PyPI version](https://badge.fury.io/py/odufrn-downloader.svg)](https://badge.fury.io/py/odufrn-downloader)

Pacote para baixar os dados do portal de [dados abertos da UFRN](dados.ufrn.br).

## Instalação
```bash
pip install odufrn-downloader
```

## Guia de uso
Veja a documentação [clicando aqui](https://odufrn.github.io/odufrn-downloader/).

Como começar a usar o pacote:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()
```

### Métodos
Abaixo estão listados os métodos disponíveis no pacote:

| Método | Descrição |
| ------ | ------- |
| `download_all` | Baixa todos os conjuntos de dados disponíveis. |
| `download_dataset` | Baixa o conjunto de dados desejado. |
| `download_datasets` | Baixa uma lista de conjuntos de dados desejado. |
| `download_from_file` | Baixa os conjuntos de dados que estão escritos em um arquivo de texto. |
| `download_group` | Baixa um grupo de conjuntos de dados desejado. |
| `download_groups` | Baixa uma lista de grupos de conjuntos de dados desejado. |
| `load_datasets` | Atualiza a lista de datasets disponíveis. |
| `load_groups` | Atualiza a lista de grupos disponíveis. |
| `list_datasets` | Lista os conjuntos de dados. |
| `list_groups` | Lista os grupos de conjuntos de dados. |
| `search_related_datasets` | Retorna uma lista de conjuntos de dados relacionados a uma entrada. |
| `search_related_groups` | Retorna uma lista de grupos de conjuntos de dados relacionados a uma entrada. |

### Exemplo
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
