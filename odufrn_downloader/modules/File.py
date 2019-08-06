import os
from .Dataset import Dataset


class File(Dataset):
    """Classe responsável pelo download de datasets a partir de um arquivo."""

    def __init__(self):
        super().__init__()

    def download_from_file(
        self, filename: str, path: str = os.getcwd(), dictionary: bool = True
    ):
        """Baixa os conjuntos de dados que estão escritos
        em um arquivo de texto.

        > Exemplo: download_from_file('datasets_ufrn.txt')

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
                    self.download_dataset(
                        datasetName.rstrip(), path, dictionary
                    )
        except IOError as ex:
            self._print_exception(ex)
