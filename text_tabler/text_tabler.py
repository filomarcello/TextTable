'''
Package useful to make old-style reports in characters and text tables, using '|' and '-'
'''
__author__ = 'marcello'

# constants
HORIZONTAL  = H = '-'
VERTICAL    = V = '|'
ANGLE       = A = '+'

class Entry(object):
    '''Abstract entry of a cell'''

    def __init__(self, content: str = ''):
        self.content = content

    # TODO inspecting methods used by Cell class to calculate the spaces
    def get_width(self) -> int:
        return len(self.content)

    def get_text(self) -> str:
        return self.content


class Cell(object):
    '''Abstract cell of a table'''

    def __init__(self, width: int, height: int, content: 'Entry' = ''):
        '''width and height correspond to the inner area of the cell.

        c = Cell(width=10, height=2) makes an area of 12 x 4 chars, due to the delimiters
        '''
        self.width = width
        self.height = height
        self.content = content

    def __str__(self):
        horiz = A + H * self.width + A +'\n'
        middle = V

        if self.content.get_width() > self.width:
            middle += self.content.get_text()[:self.width]
        else:
            middle += self.content.get_text().center(self.width)

        middle += V + '\n'

        return horiz + middle + horiz


class Table:
    '''Aabstract table'''
    pass


