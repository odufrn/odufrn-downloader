import io
import os
import sys
import json
import shutil
import unittest
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from odufrn_downloader import ODUFRNDownloader

def assert_console(output):
    """ Recebe função que printa algo na tela e realiza assert
    que verifica se foi printado """
    unit = unittest.TestCase()
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    output()
    sys.stdout = sys.__stdout__
    return unit.assertTrue(len(capturedOutput.getvalue()) > 0)

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

class Env(unittest.TestCase):
    def setUp(self):
        """ Inicia novo objeto em todo os testes """
        self.ufrn_data = ODUFRNDownloader()
        self.test_dir = 'temporary_test_dir'

    def test_can_print_exception(self):
        """ Verifica se uma exceção consegue ser printada no console """
        assert_console(lambda: self.ufrn_data._print_exception(ValueError()))

    def test_can_print_list(self):
        """ Verifica se consegue-se printar informação da lista no console """
        assert_console(lambda: self.ufrn_data._print_list("conjuntos de dados", ['discente']))

    def test_can_load_list(self):
        """ Verifica se consegue carregar uma lista advinda de requisição """
        self.assertIsInstance(self.ufrn_data._load_list('package_list'), list)

    def test_can_make_dir(self):
        """ Verifica se pode-se criar um diretório """
        self.ufrn_data._make_dir(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))
        shutil.rmtree(self.test_dir)
    
    def test_can_request_get(self):
        """ Verifica se consegue-se realizar requisição get e retornar json """
        result = False
        try:
            json.dumps(self.ufrn_data._request_get(self.ufrn_data.url_dataset + 'discentes')['resources'])
            result = True
        except:
            result = False
        self.assertTrue(result)
        
if __name__ == '__main__':
    unittest.main()