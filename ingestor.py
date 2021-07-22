from QuoteEngine import TextIngestor, CSVIngestor, PDFIngestor,\
     DocxIngestor, IngestorInterface
from typing import List


__module__ = 'QuoteEngine/ingestor.py'
__version__ = ''
__info__ = 'Adapted from/for Udacity\'s Python Nanodegree program. '
__student__ = 'Pradyumna Chawak <padu.pmc@gmail.com>'


class Ingestor(IngestorInterface):
    '''Ingest quotes from multiple file resources.'''

    ingestors = {
        'txt': TextIngestor,
        'csv': CSVIngestor,
        'docx': DocxIngestor,
        'pdf': PDFIngestor
    }

    @classmethod
    def parse(self, quote_files):
        quotes = []
        for quote_file in quote_files:
            ext = quote_file.split('.')[-1]
            quotes.extend(Ingestor.ingestors[ext].parse(quote_file))
        return quotes
