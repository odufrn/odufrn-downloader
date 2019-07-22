import requests
import json
import sys
import os


class ODUFRNDownloader():
    def __init__(self):
        self.base = 'http://dados.ufrn.br/'
        self.action = self.base + 'api/action/'
        self.dataset = self.base + 'api/rest/dataset/'

    def listPackage(self):
        """
        Lista os conjuntos de dados
        """
        try:
            print(
                json.dumps(requests.get(self.action + 'package_list').json(), indent=4)
            )
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

    def downloadPackage(self, name, path=os.getcwd()):
        """
        Exibe conjunto de dado de acordo com seu nome
        e baixa-os em pastas com o nome do respectivo
        conjunto de dado

        >>> Ex. downloadPackage('acervo-biblioteca')
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