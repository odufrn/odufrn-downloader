import io
import sys
import unittest
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from odufrn_downloader import ODUFRNDownloader


def assert_console(output):
    """ Recebe função que printa algo na tela e realiza assert
    que verifica se foi printado."""
    unit = unittest.TestCase()
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    output()
    sys.stdout = sys.__stdout__
    return unit.assertTrue(len(capturedOutput.getvalue()) > 0)
