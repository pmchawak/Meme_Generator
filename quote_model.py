
__module__ = 'QuoteEngine/quote_model.py'
__version__ = ''
__info__ = 'Adapted from/for Udacity\'s Python Nanodegree program. '
__student__ = 'Pradyumna Chawak <padu.pmc@gmail.com>'



class QuoteModel:
    '''Model of a quote:  "quote" - author '''
    def __init__(self, quote, author):
        self.body = quote
        self.author = author

    def __str__(self):
        return (f'"{self.body}" - {self.author}')



