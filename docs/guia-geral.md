# Geral
Como começar a usar o pacote:
```python
from odufrn_downloader import ODUFRNDownloader
ufrn_data = ODUFRNDownloader()
```

# Métodos
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
