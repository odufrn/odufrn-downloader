class LevenshteinMixin:
    """Mixin relacionado ao calculo de similaridade entre duas palavras."""

    def levenshtein(self, str1: list, str2: list) -> float:
        """Calcula a similaridade entre duas palavras de acordo com a distância de Levenshtein.

        Parâmetros
        ----------
        str1: list
            lista de caracteres da primeira palavra
        str2: list
            lista de caracteres da segunda palavra

        Retorno
        -------
        razão entre as palavras. Quanto mais próximo de 1, mais similares são as palavras.

        Referência
        ----------
        https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
        """
        oneago = None
        thisrow = list(range(1, len(str2) + 1)) + [0]
        for x in range(len(str1)):
            twoago, oneago, thisrow = oneago, thisrow, [0] * len(str2) + [x + 1]
            for y in range(len(str2)):
                delcost = oneago[y] + 1
                addcost = thisrow[y - 1] + 1
                subcost = oneago[y - 1] + (str1[x] != str2[y])
                thisrow[y] = min(delcost, addcost, subcost)

        lens = len(str1)+len(str2)
        ratio = (lens - thisrow[len(str2) - 1]) / lens
        return ratio

    def search_related(self, keyword: str, input_list: list) -> list:
        """Busca datasets com nomes semelhantes à palavra recebida.

        Parâmetros
        ----------
        keyword: str
            palavra-chave com a qual será feita a busca
        input_list: list
            lista com os valores que irá verificar a similaridade com keyword

        Retorno
        -------
        lista de valores com nome similares à palavra de interesse
        """
        filter_list = []
        for item in input_list:
            for word in item.split('-'):
                ratio = self.levenshtein([k for k in keyword], [d for d in word])
                if ratio > 0.87:
                    filter_list.append(item)

        return filter_list
