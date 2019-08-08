class SimpleSearchMixin:
    """Mixin relacionado ao calculo de similaridade entre duas palavras."""

    def simple_search(self, keyword: str, input_list: list) -> list:
        """Busca na input_list os elementos com nomes semelhantes
        à keyword recebida.

        Parâmetros
        ----------
        keyword: str
            palavra-chave com a qual será feita a busca.
        input_list: list
            lista com os valores que irá verificar a similaridade com keyword.

        Retorno
        -------
        lista de valores com nome similares à palavra de interesse.
        """
        filter_list = []
        for item in input_list:
            if keyword in item:
                filter_list.append(item)

        return filter_list
