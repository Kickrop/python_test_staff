# -*- coding: utf-8 -*-
import time
import random
import datetime
#import xml2json
#import json
#from lxml import etree
#from io import StringIO, BytesIO
import xml.etree.ElementTree as ET
#print "pam" + str(datetime.datetime.now())
#tree = etree.parse("test1.xml")
#tree = ET.parse('test1.xml')
tree = ET.parse('bigtest.xml')
root = tree.getroot()
#print xml2json.xml2json(tree)
#json_data = json.loads(xml2json.xml2json(tree))
#for child in root:
#    print (child.tag, child.attrib)
#print root[1][2].text
#for newdataset in root.iter('newdataset'): #iteration by elements
#    print(newdataset.text)             #
#for newdataset in root.findall('caption'): #iteration by elements
#    rank = caption.find('caption').text
    #name = country.get('name')
#    print(rank)
#for child in root:
#    print (child.tag, child.attrib)
#print root[0][2].text


#for el in root.iter('el'): #iteration by elements
#    print(el.attrib)

for fields in root.findall('fields'): #iteration by elements
    #rank = fields.find('field').text
    rank = fields.get('field')
    #name = country.get('name')
    print(rank)
