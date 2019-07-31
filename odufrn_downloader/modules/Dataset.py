import os
import requests
from .Env import Env


class Dataset(Env):
    """Classe responsável pelo download de datasets.

    Atributos
    ---------
    url_dataset: str
        a url para a consulta de datasets da API da UFRN.
    available_datasets: list
        lista de conjuntos de dados que estão disponíveis para download.
    """

    def __init__(self):
        super().__init__()

        self.url_dataset = self.url_base + 'api/rest/dataset/'
        self.available_datasets = []
        self.load_datasets()

    def load_datasets(self):
        """Atualiza lista de datasets disponíveis."""
        self.available_datasets = self._load_list('package_list')

    def list_datasets(self):
        """Lista os conjuntos de dados."""
        self._print_list("conjuntos de dados", self.available_datasets)

    def download_dataset(self, name: str, path: str = os.getcwd(), dictionary: bool = True):
        """Exibe conjunto de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado.

        > Exemplo: download_dataset('acervo-biblioteca')

        Parâmetros
        ----------
        name: str
            nome do dataset.
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual).
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True).
        """

        # Checa se o dataset está disponível
        if not (name in self.available_datasets):
            print("O conjunto de dados \"{}\" não foi encontrado.".format(name))
            return

        dataset = self._request_get(self.url_dataset + name)
        path = self._make_dir('{}/{}'.format(path, name))

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

    def download_datasets(self, datasets: list, path: str = os.getcwd(), dictionary: bool = True):
        """Exibe os conjuntos de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado.

        > Exemplo: download_datasets(['discentes', 'dados-complementares-de-discentes'])

        Parâmetros
        ----------
        datasets: list
            lista com os nomes dos datasets desejados.
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual).
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True).
        """

        for dataset in datasets:
            self.download_dataset(dataset, path, dictionary)
