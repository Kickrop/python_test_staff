# -*- coding: utf-8 -*-
#import time
#import random
#import datetime
#from xml.dom import minidom

#xmldoc = minidom.parse("bigtest.xml")
import os, sys, json
#import requests
#import urlib.request
from bs4 import BeautifulSoup
import urllib2
#path = "H:\python\Parserxml\html\staff"
#os.chdir(path)
inputfiles = os.listdir(os.getcwd())
#html_doc = inputfiles[1]
#html_doc = file = open(inputfiles[1],"r")

#soup = BeautifulSoup(open("index.html"))
# A simple python script to extract names, and emails from
# a certain online directory
#get a list of the files in the current directory
#inputfiles = os.listdir(os.getcwd())

#def postproc(inputfiles):

#for every file in the directory

#for i in inputfiles:
#call the preproc function on said file and generate the appropriate outfile
#pam = soup.find_all('tr')
#pam = soup('<label for="OG_24">')
#pam = soup.find_all('label')


#for i in range(0,3):
json_doc = file = open(inputfiles[1],"r")
pj = json.load(json_doc)
#for affil in parsed_json.findall('affil'):
#    print affil
#if 'startYear' in pj['header']:
#    print pj['header']['startYear']
#if 'title' in pj['body']['AFFIL']['data'][0]:
nafil = len (pj['body']['AFFIL']['data'])
for i in range(0,nafil):
    affil = pj['body']['AFFIL']['data'][i]['title']
    pubcount = pj['body']['AFFIL']['data'][i]['count']
    print affil + ";" + str(pubcount)
#print parsed_json
    #soup = BeautifulSoup(html_doc, 'html.parser')
    #for affil in soup.find_all('AFFIL'):
        #pam = soup.label
        #lst1 = str(label).split('>',1)[-1]
        #lst2 = str(lst1).split('<')[0]
        #lst3 = str(lst2).split(' ')[-1]
        #lst4 = str(lst2).split('(')[0]
        #lst5 = str(lst3).strip('()')
        #lst6 = str(lst4)[:-1]
        #final = (str(lst6)) + ";" + (str(lst5)) + "\n"
    #    final = soup.affil
    #    filename = 'pam' + str(i)
    #    print final + "pam"
    #    with open(filename + ".txt", "a") as myfile:
    #            myfile.write(str(i) + final)
        #file = open("pam.txt","w")
        #final = (str(lst6)) + ";" + (str(lst5)) + "\n"
        #file.write(final)
        #file.close()

#country = xmldoc.getElementsByTagName("country")[0]
#ranks = country.getElementsByTagName("rank")

#for rank in ranks:
#    print rank



#for placemark in placemarks:
#    desc = placemark.getElementsByTagName("description")[0].firstChild.data
#    lst = desc.split(":")
#    population = int(lst[1].split("<")[0])
#    coords = placemark.getElementsByTagName("coordinates")[0].firstChild.data
#    lst2 = coords.split(",")
#    longirude = float(lst2[0])
#    latitude = float(lst2[1])
#    cityName = placemark.getElementsByTagName("name")[0].firstChild.data

#    print cityName + ":", -longirude, latitude, population
