'''
Package useful to make old-style reports in characters and text tables, using '|' and '-'

version 0.1:
'''

# TODO vertical and horizontal alignment

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
        return len(self.content) # TODO implement the lines counter and return the max length line

    def get_height(self) -> int:
        return 1 # TODO implement the lines counter

    def get_text(self) -> str:
        return self.content


class Cell(object):
    '''A cell of a table'''

    def __init__(self, width: int = None, height: int = None, content: 'Entry' = ''):
        '''width and height correspond to the inner area of the cell.

        c = Cell(width=10, height=2) makes an area of 12 x 4 chars, due to the borders.
        If width and height are unspecified, they will be calculated from content
        '''
        self.content = content

        if width == None or width <= 0:
            self.width = content.get_width()
        else:
            self.width = width

        if height == None or height <= 0:
            self.height = content.get_height()
        else:
            self.height = height

    def __str__(self):
        horiz = A + H * self.width + A +'\n'
        middle = V

        # if the content is wider than the cell, truncate it
        if self.content.get_width() > self.width:
            middle += self.content.get_text()[:self.width]

        # if not, pads the content with spaces to fill and center the text in the cell
        else:
            middle += self.content.get_text().center(self.width)

        middle += V + '\n'

        return horiz + middle + horiz


class Table:
    '''Abstract table'''
    pass


