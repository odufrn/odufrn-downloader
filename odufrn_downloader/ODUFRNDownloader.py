from .modules.Group import Group
from .modules.File import File


class ODUFRNDownloader(Group, File):
    """Classe que reune todos os módulos do pacote."""

    def __init__(self):
        super().__init__()
