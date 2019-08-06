<h1 id="odufrn_downloader.ODUFRNDownloader">ODUFRNDownloader</h1>

```python
ODUFRNDownloader(self)
```
Classe responsável pelo download de datasets.

Atributos
---------
base: str
    a url para a API de dados abertos da UFRN
action: str
    a url para a página de ações da API
dataset: str
    a url para a consulta de datasets da API da UFRN
available_datasets: list
    lista de conjuntos de dados que estão disponíveis para download

Métodos
-------
_print_exception(ex: Exception)
    imprime mensagem padrão para exceções.

load_datasets()
    atualiza lista de datasets disponíveis.

list_datasets()
    lista os conjuntos de dados.

download_dataset(name: str, path: str=os.getcwd())
    exibe conjunto de dados de acordo com seu nome
    e baixa-os em pastas com o nome do respectivo
    conjunto de dado.

download_datasets(datasets: list, path: str=os.getcwd())
    exibe os conjuntos de dados de acordo com seu nome
    e baixa-os em pastas com o nome do respectivo
    conjunto de dado.

<h2 id="odufrn_downloader.ODUFRNDownloader.load_datasets">load_datasets</h2>

```python
ODUFRNDownloader.load_datasets(self)
```
Atualiza lista de datasets disponíveis.
<h2 id="odufrn_downloader.ODUFRNDownloader.list_datasets">list_datasets</h2>

```python
ODUFRNDownloader.list_datasets(self)
```
Lista os conjuntos de dados.
<h2 id="odufrn_downloader.ODUFRNDownloader.download_dataset">download_dataset</h2>

```python
ODUFRNDownloader.download_dataset(self, name:str, path:str='/home/italo/open-source/odufrn-downloader/docs')
```
Exibe conjunto de dados de acordo com seu nome
e baixa-os em pastas com o nome do respectivo
conjunto de dado.

> Exemplo: download_dataset('acervo-biblioteca')

Parâmetros
----------
name: str
    nome do dataset
path: str
    o caminho da pasta onde serão adicionados os arquivos
    (por padrão, a pasta atual)

<h2 id="odufrn_downloader.ODUFRNDownloader.download_datasets">download_datasets</h2>

```python
ODUFRNDownloader.download_datasets(self, datasets:list, path:str='/home/italo/open-source/odufrn-downloader/docs')
```
Exibe os conjuntos de dados de acordo com seu nome
e baixa-os em pastas com o nome do respectivo
conjunto de dado.

> Exemplo: download_datasets(['discentes', 'dados-complementares-de-discentes'])

Parâmetros
----------
datasets: list
    lista com os nomes dos datasets desejados
path: str
    o caminho da pasta onde serão adicionados os arquivos
    (por padrão, a pasta atual)

