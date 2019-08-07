from .utils import *

class Group(unittest.TestCase):
    def setUp(self):
        """ Inicia novo objeto em todo os testes """
        self.ufrn_data = ODUFRNDownloader()

    def test_list_groups(self):
        """ Verifica se a lista de grupos é impressa na tela """
        assert_console(self.ufrn_data.list_groups)

    def test_load_groups(self):
        """ Verifica se a lista de grupos é carregada no objeto """
        self.ufrn_data.load_datasets()
        self.assertTrue(len(self.ufrn_data.available_datasets) > 0)

    def test_get_packages_group(self):
        """ Verifica se a lista de datasets em um grupo é retornada """
        self.assertTrue(len(self.ufrn_data.get_datasets_group('despesas-e-orcamento')) > 0)
