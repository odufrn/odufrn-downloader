from utils import *


class Dataset(unittest.TestCase):
    def setUp(self):
        """ Inicia novo objeto em todo os testes """
        self.ufrn_data = ODUFRNDownloader()

    def test_can_list_datasets(self):
        """ Verifica se a lista de datasets é impressa na tela """
        assert_console(self.ufrn_data.list_datasets)

    def test_can_load_datasets(self):
        """ Verifica se a lista de datasets é carregada no objeto """
        self.ufrn_data.load_datasets()
        self.assertTrue(len(self.ufrn_data.available_datasets) > 0)


if __name__ == '__main__':
    unittest.main()
