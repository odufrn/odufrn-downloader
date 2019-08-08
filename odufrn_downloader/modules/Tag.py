import os
import requests
from .Env import Env
from ..mixins.FilterMixin import FilterMixin


class Tag(Env, FilterMixin):
    """Classe responsável pelo tratamento de pacotes por etiqueta.

    Atributos
    ---------
    url_tag: str
        a url para a consulta de pacotes da API da UFRN.
    available_tags: list
        lista de etiquetas que estão disponíveis.
    """

    def __init__(self):
        super().__init__()

        self.url_tag = self.url_base + 'api/rest/tag'
        self.available_tags = []
        self.load_tags()

    def load_tags(self):
        """Atualiza lista de etiquetas disponíveis. """
        self.available_tags = self._load_list('tag_list')

    def search_by_tag(self, tag: str) -> list:
        """ """
        tags = self.search_related(tag, self.available_tags, False)
        packages = []
        for key in tags:
            url = self.url_tag + "/" + key
            print(url)
            package = self._request_get(url)
            packages += package

        return packages
