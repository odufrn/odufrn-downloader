from .filters.LevenshteinMixin import LevenshteinMixin
from .filters.SimpleSearchMixin import SimpleSearchMixin


class FilterMixin(LevenshteinMixin, SimpleSearchMixin):
    """Mixin que engloba os métodos de filtros."""
