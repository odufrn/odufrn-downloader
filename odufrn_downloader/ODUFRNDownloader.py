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

    download_dataset(name: str, path: str=os.getcwd())
        exibe conjunto de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado.

    download_datasets(datasets: list, path: str=os.getcwd())
        exibe os conjuntos de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado.
    """

    def __init__(self):
        self.base = 'http://dados.ufrn.br/'
        self.action = self.base + 'api/action/'
        self.dataset = self.base + 'api/rest/dataset/'
        self.load_datasets()

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

    def list_datasets(self):
        """Lista os conjuntos de dados."""
        print("Os conjuntos de dados disponíveis são:")
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(self.available_datasets)

    def download_dataset(self, name: str, path: str = os.getcwd(), dictionary: bool = True):
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
                if not dictionary and 'Dicion' in resource['name']:
                    continue
                    
                print("Baixando {}...".format(resource['name']))
                file_path = '{}/{}.{}'.format(
                    path, resource['name'], resource['format'].lower()
                )

                with open(file_path, 'wb') as f:
                    f.write(requests.get(resource['url']).content)
        except Exception as ex:
            self._print_exception(ex)

    def download_datasets(self, datasets: list, path: str = os.getcwd()):
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
        """

        for dataset in datasets:
            self.download_dataset(dataset, path)
