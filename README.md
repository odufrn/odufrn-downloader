# Open Data UFRN Downloader
Pacote para baixar os dados do portal de dados abertos da UFRN.

```bash
pip install odufrn-downloader
```

## Utilizando

```python
from dadosAbertosUFRNDownloader import DadosAbertosUFRNDownloader
ufrn_data = DadosAbertosUFRNDownloader()

# Lista os conjuntos de dados
ufrn_data.listPackage()

# Baixa um conjunto de dado
ufrn_data.downloadPackage('discentes')
```