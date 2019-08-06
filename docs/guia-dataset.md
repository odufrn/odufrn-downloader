# Dataset
Os métodos aqui apresentados são referentes ao uso de _datasets_ (listagem, download, etc).

## download_all
Baixa todos os conjuntos de dados disponíveis.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |
| `dictionary` | `bool` | `True` | Indica se é para baixar o dicionário dos dados. |
| `years` | `list[int]` | `None` | Define os anos dos dados que serão baixados. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar todos os datasets de 2013 a 2018, sem dicionário
ufrn_data.download_all(dictionary=False, years=list(range(2013,2019)))
```

## download_dataset
Baixa o conjunto de dados desejado.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `name` | `str` | - | Nome do dataset que se deseja baixar. |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |
| `dictionary` | `bool` | `True` | Indica se é para baixar o dicionário dos dados. |
| `years` | `list[int]` | `None` | Define os anos dos dados que serão baixados. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar os datasets de discentes sem dicionário
ufrn_data.download_dataset('discentes', dictionary=False)
```

## download_datasets
Baixa uma lista de conjuntos de dados desejado.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `datasets` | `list[str]` | - | Lista com os nomes dos datasets desejados. |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |
| `dictionary` | `bool` | `True` | Indica se é para baixar o dicionário dos dados. |
| `years` | `list[int]` | `None` | Define os anos dos dados que serão baixados. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar os datasets de discentes e seus dados complementares, sem dicionários
ufrn_data.download_datasets(['discentes', 'dados-complementares-de-discentes'], dictionary=False)
```
            
## download_from_file
Baixa os conjuntos de dados que estão escritos em um arquivo de texto.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `filename` | `str` | - | Nome do arquivo que contêm os datasets. |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |
| `dictionary` | `bool` | `True` | Indica se é para baixar o dicionário dos dados. |
| `years` | `list[int]` | `None` | Define os anos dos dados que serão baixados. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar os datasets escritos em um arquivo
ufrn_data.download_from_file('discentes_ufrn.txt')
```

**Observação**: Cada _dataset_ deve ser declarado em uma linha, dessa forma, um arquivo com os _datasets_ de discentes ficaria assim ("discentes_ufrn.txt"):
```text
discentes
dados-complementares-de-discentes
dados-socio-economicos-de-discentes
```

## load_datasets
Atualiza a lista de datasets disponíveis. A lista com esses valores é a variável `available_datasets`.

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Atualizando a lista de datasets disponíveis
ufrn_data.load_datasets()
# Acessando a lista de datasets disponíveis
ufrn_data.available_datasets
```

## list_datasets
Lista os conjuntos de dados. Apresenta os elementos presentes na lista `available_datasets`.

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Apresentando a lista de datasets disponíveis
ufrn_data.list_datasets()
```

## search_related_datasets
Retorna uma lista de conjuntos de dados relacionados a uma entrada.
Atualmente usa-se o cálculo de Levenshtein para verificar a similaridade
entre a entrada e os nomes dos datasets.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `keyword` | `str` | - | Palavra-chave com a qual será feita a busca. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Procurar datasets relacionados a discente
list_discentes = ufrn_data.search_related_datasets('discente')
print(list_discentes)

# Output:
# ['dados-complementares-de-discentes', 'dados-socio-economicos-de-discentes', 'discentes']
```
