import xml.dom.minidom as dom
from functools import reduce

DomTree = dom.parse('demo.xml').documentElement
books = DomTree.getElementsByTagName('book')
print(len(books))

authors = DomTree.getElementsByTagName('author')
print(authors[0].childNodes[0].data)
print(authors[0].childNodes[0].nodeValue)

print(books[1].getAttribute('category'))


import xml.etree.ElementTree as ET

Tree = ET.parse('demo.xml')
print(type(Tree))
books = Tree.getiterator('book')
print(type(books[0]))

authors = Tree.getiterator('author')
print(authors[0].text)

print(books[1].attrib['category'])

print(Tree.find(".//book[@category='web']/price").text)
print(type(Tree.findall(".//book[@category='web']/price")))
for price in Tree.findall(".//book[@category='web']/price"):
    print(price.text)

for title in Tree.findall(".//book[@category='web']/title"):
    print(title.attrib['lang'])


import json
Tree = ET.parse('test.xml')
pro_name = [p.tag for p in Tree.find("./project").getchildren()]

data = {}
for p in pro_name:
    h = reduce(lambda x, y:int(x)+int(y), [a.text for a in Tree.findall(".//%s//h"%p)])
    m = reduce(lambda x, y: int(x) + int(y), [a.text for a in Tree.findall(".//%s//m" % p)])
    l = reduce(lambda x, y: int(x) + int(y), [a.text for a in Tree.findall(".//%s//l" % p)])
    data[p] = h + m + l
print(data)
print(json.dumps(data, indent=4))