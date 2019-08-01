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
tree = ET.parse('test1.xml')
root = tree.getroot()
#print xml2json.xml2json(tree)
#json_data = json.loads(xml2json.xml2json(tree))
#for child in root:
#    print (child.tag, child.attrib)
print root[0][1].text
