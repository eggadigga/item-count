#!python3
## itemCount.py - output number of items repeated

import pyperclip, os, pprint

itemText = pyperclip.paste().split('\n')

itemsDic = {}
for x in itemText:
    itemsDic.setdefault(x, 0)
    itemsDic[x] = 1 + itemsDic[x]

f = 'itemsCounted.csv'

txtFile = open(f, 'w')
txtFile.write('Item,Count\n')
for k, v in itemsDic.items():
    txtFile.write(k + ',' + str(v) + '\n')

txtFile.close