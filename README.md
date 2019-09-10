# Open Data UFRN Downloader
<a href="https://pypi.org/project/odufrn-downloader/">
  <img alt="PyPI" src="https://img.shields.io/pypi/v/odufrn-downloader?color=brightgreen">
</a>
<a href="https://travis-ci.org/odufrn/odufrn-downloader">
  <img alt="Build" src="https://travis-ci.org/odufrn/odufrn-downloader.svg?branch=master">
</a>
<a href="https://coveralls.io/github/odufrn/odurfn-downloader?branch=master">
  <img alt="Coverage Status" src="https://img.shields.io/coveralls/odufrn/odufrn-downloader?color=brightgreen">
</a>
<a href="https://github.com/odufrn/odufrn-downloader/blob/master/LICENSE">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-brightgreen.svg">
</a>

Pacote para baixar os dados do portal de [dados abertos da UFRN](http://dados.ufrn.br/).

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
| `download_package` | Baixa o pacote de dados desejado. |
| `download_packages` | Baixa uma lista de pacotes de dados desejado. |
| `download_from_file` | Baixa os pacotes de dados que estão escritos em um arquivo de texto. |
| `download_group` | Baixa um grupo de conjuntos de dados desejado. |
| `download_groups` | Baixa uma lista de grupos de pacotes de dados desejado. |
| `load_packages` | Atualiza a lista de pacotes disponíveis. |
| `load_groups` | Atualiza a lista de grupos disponíveis. |
| `load_tags` | Atualiza lista de etiquetas disponíveis. |
| `print_files_from_package` | Imprime no terminal a lista de arquivos referentes ao pacote de entrada. |
| `print_files_from_group` | Imprime no terminal a lista de arquivos referentes ao grupo de entrada. |
| `print_packages` | Imprime os pacotes de dados. |
| `print_groups` | Imprime os grupos de conjuntos de dados. |
| `print_tags` | Imprime as etiquetas. |
| `search_by_tag` | Retorna uma lista de pacotes de dados relacionados a uma etiqueta. |
| `search_related_packages` | Retorna uma lista de pacotes de dados relacionados a uma entrada. |
| `search_related_groups` | Retorna uma lista de grupos de conjuntos de dados relacionados a uma entrada. |

### Exemplo
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Lista os conjuntos de dados
ufrn_data.print_packages()

# Baixa um conjunto de dados
ufrn_data.download_package('discentes')

# Baixa uma lista de conjuntos de dados
packages = ['discentes', 'dados-complementares-de-discentes', 'dados-socio-economicos-de-discentes']
ufrn_data.download_packages(packages)
```
