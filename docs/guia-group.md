# Group
Os métodos aqui apresentados são referentes ao uso de grupos de conjuntos de dados (listagem, download, etc).

## download_group
Baixa um grupo de conjuntos de dados desejado.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `name` | `str` | - | Nome do grupo que se deseja baixar. |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |
| `dictionary` | `bool` | `True` | Indica se é para baixar o dicionário dos dados. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar os datasets do grupo de pessoas
ufrn_data.download_group('pessoas')
```

## download_groups
Baixa uma lista de grupos de conjuntos de dados desejado.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `groups` | `list[str]` | - | Lista com os nomes dos grupos desejados. |
| `path` | `str` | `os.getcwd()` | O caminho da pasta onde serão adicionados os arquivos. |
| `dictionary` | `bool` | `True` | Indica se é para baixar o dicionário dos dados. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Baixar os datasets de pesquisa e despesas e orçamentos, sem dicionários
ufrn_data.download_groups(['pesquisa', 'despesas-e-orcamento'], dictionary=False)
```

## load_groups
Atualiza a lista de grupos disponíveis. A lista com esses valores é a variável `available_groups`.

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Atualizando a lista de grupos disponíveis
ufrn_data.load_groups()
# Acessando a lista de grupos disponíveis
ufrn_data.available_groups
```

## list_groups
Lista os grupos de conjuntos de dados. Apresenta os elementos presentes na lista `available_groups`.

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Apresentando a lista de grupos de datasets disponíveis
ufrn_data.list_groups()
```

## search_related_groups
Retorna uma lista de grupos de conjuntos de dados relacionados a uma entrada.
Atualmente usa-se o cálculo de Levenshtein para verificar a similaridade
entre a entrada e os nomes dos grupos.

**Parâmetros**:

| Parâmetro | Tipo | Valor padrão | Descrição |
| --------- | ---- | ------------ | --------- |
| `keyword` | `str` | - | Palavra-chave com a qual será feita a busca. |

**Exemplo**:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()

# Procurar datasets relacionados a discente
list_groups = ufrn_data.search_related_groups('pesquis')
print(list_groups)

# Output:
# ['pesquisa']
```