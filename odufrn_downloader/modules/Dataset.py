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

    def _levenshtein(self, str1, str2):
        """Calcula a similaridade entre duas palavras de acordo com a distância de Levenshtein.

        Parâmetros
        ----------
        str1: list
            lista de caracteres da primeira palavra
        str2: list
            lista de caracteres da segunda palavra

        Retorno
        -------
        razão entre as palavras. Quanto mais próximo de 1, mais similares são as palavras.

        Referência
        ----------
        https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
        """
        oneago = None
        thisrow = list(range(1, len(str2) + 1)) + [0]
        for x in range(len(str1)):
            twoago, oneago, thisrow = oneago, thisrow, [0] * len(str2) + [x + 1]
            for y in range(len(str2)):
                delcost = oneago[y] + 1
                addcost = thisrow[y - 1] + 1
                subcost = oneago[y - 1] + (str1[x] != str2[y])
                thisrow[y] = min(delcost, addcost, subcost)

        lens = len(str1)+len(str2)
        ratio = (lens - thisrow[len(str2) - 1]) / lens
        return ratio

    def _search_related_datasets(self, key: str) -> list:
        """Busca datasets com nomes semelhantes à palavra recebida.

        Parâmetros
        ----------
        key: str
            palavra-chave com a qual será feita a busca

        Retorno
        -------
        lista de datasets com nome similares à palavra de interesse
        """
        datasets = []
        for dataset in self.available_datasets:
            for word in dataset.split('-'):
                ratio = self._levenshtein([k for k in key], [d for d in word])
                if ratio > 0.87:
                    datasets.append(dataset)

        return datasets

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

    def download_datasets(self, datasets: list, path: str = os.getcwd(),
                          dictionary: bool = True):
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
            flag para baixar o dicionário dos dados (por padrão, True).
        """

        for dataset in datasets:
            self.download_dataset(dataset, path, dictionary)

    def download_related_datasets(self, key: str):
        """Baixa conjuntos de dados que possuam nomes
        semelhantes à palavra recebida.

        > Exemplo: download_related_datasets('discente')

        Parâmetros
        ----------
        key: str
            palavra-chave com a qual será feita a busca
        """
        # Busca nomes de datasets semelhantes à palavra passada
        related = self._search_related_datasets(key)

        # Imprime exceção se não houver datasets similares
        if len(related) == 0:
            print("Não há nenhum conjunto de dados \
                    semelhante a \"{}\".".format(key))
            return
