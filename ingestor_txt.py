from .ingestor_interface import IngestorInterface
from .quote_model import QuoteModel
from typing import List


__module__ = 'QuoteEngine/ingestor_txt.py'
__version__ = ''
__info__ = 'Adapted from/for Udacity\'s Python Nanodegree program. '
__student__ = 'Pradyumna Chawak <padu.pmc@gmail.com>'



class TextIngestor(IngestorInterface):
    '''Ingests quotes from a text file'''

    extensions_list = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot Ingest '+path)
        quotes = []
        with open(path) as fin:
            for line in fin:
                quote, author = line.split(' - ')
                quote = cls.sanitize(quote)
                author = cls.sanitize(author)
                quotes.append(QuoteModel(quote, author))
        return quotes
