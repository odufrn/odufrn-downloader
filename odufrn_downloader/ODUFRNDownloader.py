import requests
import json
import sys
import os
import pprint


class ODUFRNDownloader():
    """Classe responsável pelo download de datasets.

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

    download_dataset(name: str, path: str=os.getcwd(), dictionary: bool = True)
        exibe conjunto de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado. Podendo setar se deseja baixar
        o dicionário dos dados

    download_datasets(datasets: list, path: str=os.getcwd(), dictionary: bool = True, years: array = [])
        exibe os conjuntos de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado. Podendo setar se deseja baixar
        o dicionário dos dados e os anos que podem ser baixados

    def download_from_file(self, filename: str, path: str = os.getcwd(), dictionary: bool = True):
        Baixa os conjuntos de dados que estão escrito
        em um arquivo de texto.
    """

    def __init__(self):
        self.base = 'http://dados.ufrn.br/'
        self.action = self.base + 'api/action/'
        self.dataset = self.base + 'api/rest/dataset/'
        self.group = self.base + 'api/rest/group/'
        self.load_datasets()
        self.load_groups()

    def _print_exception(self, ex: Exception):
        """Imprime mensagem padrão para exceções."""
        print('\033[91m{}\033[0m'.format(ex))
        print(
            "Ocorreu algum erro durante o download do dataset. "
            "Verifique sua conexão, o nome do conjunto de dados "
            "e tente novamente."
        )

    def load_datasets(self):
        """Atualiza lista de datasets disponíveis."""
        try:
            packages = requests.get(self.action + 'package_list').json()

            # Atualiza lista
            self.available_datasets = packages['result']
        except Exception as ex:
            self._print_exception(ex)

    def load_groups(self):
        """Atualiza lista de grupos disponíveis."""
        try:
            packages = requests.get(self.action + 'group_list').json()

            # Atualiza lista
            self.available_groups = packages['result']
        except Exception as ex:
            self._print_exception(ex)

    def list_datasets(self):
        """Lista os conjuntos de dados."""
        print("Os conjuntos de dados disponíveis são:")
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.available_datasets)
        
    def list_groups(self):
        """Lista os grupos de dados."""
        print("Os grupos de dados disponíveis são:")
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.available_groups)

    def download_dataset(self, name: str, path: str = os.getcwd(), dictionary: bool = True, years=[]):
        """Exibe conjunto de dados de acordo com seu nome
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
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True)
        years: array
            Define os anos dos dados que serão baixados, se existir realiza-se o download
        """

        # Checa se o dataset está disponível
        if not (name in self.available_datasets):
            print("O conjunto de dados \"{}\" não foi encontrado.".format(name))
            return

        request_dataset = requests.get(self.dataset + name)

        dataset = request_dataset.json()
        path = os.path.join(path, name)

        if not os.path.exists(path):
            os.makedirs(path)

        try:
            for resource in dataset['resources']:
                year = [year for year in years if resource['name'].find(str(year)) != -1]                   
                
                if not dictionary and 'Dicion' in resource['name']:
                    continue    

                if years == [] or len(year) > 0:    
                    print("Baixando {}...".format(resource['name']))
                    file_path = '{}/{}.{}'.format(
                        path, resource['name'], resource['format'].lower()
                    )

                    with open(file_path, 'wb') as f:
                        f.write(requests.get(resource['url']).content)
        except Exception as ex:
            self._print_exception(ex)

    def download_datasets(self, datasets: list, path: str = os.getcwd(), dictionary: bool = True, years=[]):
        """Exibe os conjuntos de dados de acordo com seu nome
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
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True)  
        """

        for dataset in datasets:
            self.download_dataset(dataset, path, dictionary, years)
    
    def download_group(self, name: str, path: str = os.getcwd(), dictionary: bool = True):
        """Exibe grupo de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        grupo de dados.

        > Exemplo: download_group('pessoas')

        Parâmetros
        ----------
        name: str
            nome do grupo
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual)
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True)    
        """

        # Checa se o grupo está disponível
        if not (name in self.available_groups):
            print("O grupo de dados \"{}\" não foi encontrado.".format(name))
            return

        request_group = requests.get(self.group + name)
        groups = request_group.json()

        path = os.path.join(path, name)

        if not os.path.exists(path):
            os.makedirs(path)

        try:
            for package in groups['packages']:
                self.download_dataset(package, path, dictionary)
                
        except Exception as ex:
            self._print_exception(ex)        

    def download_groups(self, groups: list, path: str = os.getcwd(), dictionary: bool = True):
        """Exibe os grupos de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        grupo de dados.

        > Exemplo: download_groups(['biblioteca', 'ensino'])

        Parâmetros
        ----------
        groups: list
            lista com os nomes dos datasets desejados
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual)
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True)  
        """

        for group in groups:
            self.download_group(group, path, dictionary)

    def download_from_file(self, filename: str, path: str = os.getcwd(), dictionary: bool = True):
        """Baixa os conjuntos de dados que estão escrito
        em um arquivo de texto.

        > Exemplo: download_from_file('arquivo_teste.txt')

        Parâmetros
        ----------
        filename: str
            nome do arquivo que contêm os datasets
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual)
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True)
        """
        try:
            with open(filename, 'r') as file:
                for datasetName in file:
                    self.download_dataset(datasetName.rstrip(), path, dictionary)
        except IOError as ex:
            self._print_exception(ex)
