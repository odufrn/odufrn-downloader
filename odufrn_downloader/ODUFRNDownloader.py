import requests
import json
import sys
import os


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

    Métodos
    -------
    list_datasets()
        Lista os conjuntos de dados.

    download_dataset(name, path=os.getcwd())
        Exibe conjunto de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado.

    download_datasets(name, path=os.getcwd())
        Exibe os conjuntos de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado.
    """

    def __init__(self):
        self.base = 'http://dados.ufrn.br/'
        self.action = self.base + 'api/action/'
        self.dataset = self.base + 'api/rest/dataset/'

    def list_datasets(self):
        """Lista os conjuntos de dados."""
        try:
            print(
                json.dumps(requests.get(self.action + 'package_list').json(), indent=4)
            )
        except requests.exceptions.RequestException as ex:
            print(ex)
            sys.exit(1)

    def download_dataset(self, name: str, path: str = os.getcwd()):
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
        request_dataset = requests.get(self.dataset + name)

        if request_dataset.status_code == 404:
            print("O conjunto de dados \"{}\" não foi encontrado.".format(name))
            return

        dataset = request_dataset.json()
        path = os.path.join(path, name)

        if not os.path.exists(path):
            os.makedirs(path)

        try:
            for resource in dataset['resources']:
                print("Baixando {}...".format(resource['name']))
                file_path = '{}/{}.{}'.format(
                    path, resource['name'], resource['format'].lower()
                )

                with open(file_path, 'wb') as f:
                    f.write(requests.get(resource['url']).content)
        except Exception as ex:
            print('\033[91m{}\033[0m'.format(ex))
            print(
                "Ocorreu algum erro durante o download do dataset. "
                "Verifique sua conexão, o nome do conjunto de dados "
                "e tente novamente."
            )

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
