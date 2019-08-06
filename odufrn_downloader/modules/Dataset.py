import os
import requests
from .Env import Env
from ..mixins.LevenshteinMixin import LevenshteinMixin


class Dataset(Env, LevenshteinMixin):
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

    def download_dataset(self, name: str, path: str = os.getcwd(),
                         dictionary: bool = True, years: list = None):
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
        years: list
            Define os anos dos dados que serão baixados, se existir realiza-se o download.
        """

        # Checa se o dataset está disponível
        if not (name in self.available_datasets):
            print("O conjunto de dados \"{}\" não foi encontrado.".format(name))
            return

        dataset = self._request_get(self.url_dataset + name)
        path = self._make_dir('{}/{}'.format(path, name))

        try:
            for resource in dataset['resources']:
                if years and len(years) == 0:
                    break

                year_find = False
                if years:
                    for key, year in enumerate(years):
                        if str(year) in resource['name']:
                            year_find = True
                            del (years[key])

                if not dictionary and 'Dicion' in resource['name']:
                    continue

                if years is None or year_find:
                    print("Baixando {}...".format(resource['name']))
                    file_path = '{}/{}.{}'.format(
                        path, resource['name'], resource['format'].lower()
                    )

                    with open(file_path, 'wb') as f:
                        f.write(requests.get(resource['url']).content)
        except Exception as ex:
            self._print_exception(ex)

    def download_datasets(self, datasets: list, path: str = os.getcwd(),
                          dictionary: bool = True, years: list = None):
        """Exibe os conjuntos de dados de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado.

        > Exemplo: download_datasets(['discentes', \
            'dados-complementares-de-discentes'])

        Parâmetros
        ----------
        datasets: list
            lista com os nomes dos datasets desejados.
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual).
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True)
        years: list
            define os anos dos dados que serão baixados, se existir realiza-se o download.
        """

        for dataset in datasets:
            self.download_dataset(dataset, path, dictionary, years)

    def search_related_datasets(self, keyword: str) -> list:
        """Procura os conjuntos de dados que possuam nomes
        semelhantes à palavra recebida.

        > Exemplo: search_related_datasets('discente')

        Parâmetros
        ----------
        keyword: str
            palavra-chave com a qual será feita a busca
        """
        # Busca nomes de datasets semelhantes à palavra passada
        related = self.search_related(keyword, self.available_datasets)

        # Imprime exceção se não houver datasets similares
        if not len(related):
            print("Não há nenhum conjunto de dados semelhante a \"{}\".".format(keyword))

        return related
        
    def download_all(self, path: str = os.getcwd(),
                          dictionary: bool = True, years: list = None):
        """Exibe os todos conjuntos de dados e baixa-os 
        em pastas com o nome do respectivo conjunto de dado.

        > Exemplo: download_all(dictionary = False, years = list(range(2009, 2014)))

        Parâmetros
        ----------
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual).
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True)
        years: list
            define os anos dos dados que serão baixados, se existir realiza-se o download.
        """
        
        self.download_datasets(self.available_datasets, path, dictionary, years)
