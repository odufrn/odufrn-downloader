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
        list_package()
            Lista os conjuntos de dados.

        download_package(name, path=os.getcwd())
            Exibe conjunto de dado de acordo com seu nome
            e baixa-os em pastas com o nome do respectivo
            conjunto de dado
    """

    def __init__(self):
        self.base = 'http://dados.ufrn.br/'
        self.action = self.base + 'api/action/'
        self.dataset = self.base + 'api/rest/dataset/'

    def list_package(self):
        """Lista os conjuntos de dados. """
        try:
            print(
                json.dumps(requests.get(self.action + 'package_list').json(), indent=4)
            )
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

    def download_package(self, name: str, path=os.getcwd(): str):
        """
        Exibe conjunto de dado de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado

        >>> Ex. downloadPackage('acervo-biblioteca')

        Parâmetros
        ----------
        name: str
            nome do dataset
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual)
        """

        dataset = requests.get(self.dataset + name).json()

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
        except:
            # shutil.rmtree(path)
            print(
                "Ocorreu algum erro durante o download do pacote "
                "verifique sua conexão, o nome do conjunto de dados "
                "e tente novamente"
            )
