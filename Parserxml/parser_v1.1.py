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
tree = ET.parse('bigtest.xml')
#tree = ET.parse('test1.xml')
root = tree.getroot()
#print xml2json.xml2json(tree)
#json_data = json.loads(xml2json.xml2json(tree))

#field = root.findall('./table/fields/field')
#fields = root.findall('./table/fields')


#for country in root.findall('country'):
for table in root.findall('field'):
    #tid = table.get('id')
    cap = table.get('caption')
    #country = country.get('name')
    print cap


#for field in fields:
#    name = fields.get('name')
#    print name


#for child in root:
    #print (child.tag, child.attrib)
#print root[1][2].text



#for el in root.iter('el'): #iteration by elements
#    print(el.attrib)             #
#for country in root.findall('country'): #iteration by elements
#    rank = country.find('./rank').text
#    name = country.get('name')
#    print(rank)
