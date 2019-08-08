from .utils import *


class Group(unittest.TestCase):
    def setUp(self):
        """Inicia novo objeto em todo os testes """
        self.ufrn_data = ODUFRNDownloader()

    def test_list_groups(self):
        """Verifica se a lista de grupos é impressa na tela """
        assert_console(self.ufrn_data.list_groups)

    def test_load_groups(self):
        """Verifica se a lista de grupos é carregada no objeto """
        self.ufrn_data.load_groups()
        self.assertTrue(len(self.ufrn_data.available_groups) > 0)

    def test_get_packages_group(self):
        """Verifica se a lista de datasets em um grupo é
        retornada
        """
        group = 'despesas-e-orcamento'
        self.assertTrue(len(self.ufrn_data.get_packages_group(group)) > 0)

    def test_search_groups(self):
        """Verifica se a procura por grupos está funcionando."""
        list_groups = self.ufrn_data.search_related_groups('pesquis')
        self.assertTrue(len(list_groups) == 1)
        list_groups = self.ufrn_data.search_related_groups('pesq', True)
        self.assertTrue(len(list_groups) == 1)
        list_groups = self.ufrn_data.search_related_groups('pesq')
        self.assertTrue(len(list_groups) == 0)
