# -*- coding: utf-8 -*-
import time
import random
import datetime
from xml.dom import minidom

xmldoc = minidom.parse("test1.xml")

#rank = xmldoc.getElementsByTagName("rank")[0]

country = xmldoc.getElementsByTagName("country")[0]
ranks = country.getElementsByTagName("rank")
#pam = ranks.getElementsByTagName("pam")
for rank in ranks:
    print rank
#print str(rank)


for placemark in placemarks:
    desc = placemark.getElementsByTagName("description")[0].firstChild.data
    lst = desc.split(":")
    population = int(lst[1].split("<")[0])
    coords = placemark.getElementsByTagName("coordinates")[0].firstChild.data
    lst2 = coords.split(",")
    longirude = float(lst2[0])
    latitude = float(lst2[1])
    cityName = placemark.getElementsByTagName("name")[0].firstChild.data

    print cityName + ":", -longirude, latitude, population
