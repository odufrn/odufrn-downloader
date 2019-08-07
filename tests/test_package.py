from .utils import *


class Package(unittest.TestCase):
    def setUp(self):
        """ Inicia novo objeto em todo os testes """
        self.ufrn_data = ODUFRNDownloader()

    def test_can_list_packages(self):
        """ Verifica se a lista de packages é impressa na tela """
        assert_console(self.ufrn_data.list_packages)

    def test_can_load_packages(self):
        """ Verifica se a lista de packages é carregada no objeto """
        self.ufrn_data.load_packages()
        self.assertTrue(len(self.ufrn_data.available_packages) > 0)
