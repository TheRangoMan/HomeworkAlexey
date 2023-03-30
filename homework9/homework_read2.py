from pprint import pprint
from homework_read import Textdata

t = Textdata().readfile('').createresult()
pprint(t.maxincome())
pprint(t.map)