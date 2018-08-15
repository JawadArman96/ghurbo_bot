#!/usr/bin/python3
from importlib import reload

from idna import unicode
import re
import sys
import datetime
reload(sys)
#sys.setdefaultencoding('utf-8')
# Open a file
fo = open("wh_question.txt",encoding='utf-8',mode= "r")

for line in fo:
    print(line)


# Close opened file
fo.close()