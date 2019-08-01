# -*- coding: utf-8 -*-
#import time
#import random
#import datetime
#from xml.dom import minidom
import time
import codecs
import os, sys, json
from bs4 import BeautifulSoup
import urllib2
t = time.ctime()
path = "H:\python\json\scopus"
os.chdir(path)
inputfiles = os.listdir(os.getcwd())
nfdir = len(inputfiles)

print "in progress", t

filename = "outputdata_scopus_url"
for j in range(0,nfdir):
    json_doc = file = open(inputfiles[j],"r")
    pj = json.load(json_doc)
    name = inputfiles[j]
    name1 = name.split('_')
    country = name1[-3]
    subjmain = name1[-2]
    nafil = len (pj['body']['AFFIL']['data'])
    for i in range(0,nafil):
        affil = pj['body']['AFFIL']['data'][i]['title']
        pubcount = pj['body']['AFFIL']['data'][i]['count']
        #counturl = pj['body']['AFFIL']['data'][i]['counturl']
        #titleurl = pj['body']['AFFIL']['data'][i]['titleurl']
        id1 = pj['body']['AFFIL']['data'][i]['id']
        #print country + ";" + str(subjmain) + ";" + affil + ";" + str(pubcount)
        with open(filename + ".txt", "a") as myfile:
                myfile.write((country + "$" + str(subjmain) + "$" + affil + "$" + str(pubcount) + "$" + id1 + "\n").encode('utf-8'))
#end
t1 = time.ctime()
print "success", t1
