import os
from .Package import Package


class File(Package):
    """Classe responsável pelo download de pacotes a partir de um arquivo."""

    def __init__(self):
        super().__init__()

    def download_from_file(self, filename: str, path: str = os.getcwd(),
                           dictionary: bool = True, years: list = None):
        """Baixa os pacotes de dados que estão escritos
        em um arquivo de texto.

        > Exemplo: download_from_file('packages_ufrn.txt')

        Parâmetros
        ----------
        filename: str
            nome do arquivo que contêm os pacotes.
        path: str
            o caminho da pasta onde serão adicionados os arquivos
            (por padrão, a pasta atual).
        dictionary: bool
            flag para baixar o dicionário dos dados (por padrão, True).
        years: list
            define os anos dos dados que serão baixados, se existir
            realiza-se o download
        """
        try:
            with open(filename, 'r') as file:
                for packageName in file:
                    self.download_package(
                        packageName.rstrip(), path, dictionary, years
                    )
        except IOError as ex:
            self._print_exception(ex)
