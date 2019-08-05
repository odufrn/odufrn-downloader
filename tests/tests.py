import io
import sys
import unittest
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from odufrn_downloader import ODUFRNDownloader

class ODUFRNDownloaderTest(unittest.TestCase):
    def setUp(self):
        """ Inicia novo objeto em todo os testes """
        self.ufrn_data = ODUFRNDownloader()

    def test_can_list_datasets(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.ufrn_data.list_datasets()
        sys.stdout = sys.__stdout__
        self.assertTrue(len(capturedOutput.getvalue()) > 0)

if __name__ == '__main__':
    unittest.main()