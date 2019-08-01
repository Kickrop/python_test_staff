# -*- coding: utf-8 -*-
import time
import random
import json
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome import service
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

from selenium.common.exceptions import NoSuchElementException



#countryname = "Argentina"
subjarea = "subjarea(ENER)"

country_from_file = []
with open('country.txt','r') as inf:
    for line in inf:
        country_from_file.append(eval('line'))



dicts_from_file = []
#with open('scopus_subj_names_big.txt','r') as inf:
with open('scopus_subj_names_big_subjarea.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval('line'))

s = 0
num_lines = sum(1 for line in open('scopus_subj_names_big.txt'))
do = num_lines#160

def gettothepageandsavetofile():
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""Russian Federation"") and subjarea(ENER)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry( A* or B* or c* or d* or e* or f* or g* or h* or "Iceland" or "Indonesia" or "Iran" or "Iraq" or "Ireland"or "Israel"or "Italy" or j* or k* or l* or m* or n* or o* or p* or q* or r* or s* or t* or u* or v* or w* or x* or y* or z*) and subjarea(ENER)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""Russian Federation"") and subjarea(ENER)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry( A* or "Bahamas" or "Bahrain" or "Bangladesh" or "Barbados" or "Belarus" or "Belgium" or "Belize" or "Benin" or "Bermuda" or "Bhutan" or "Bolivia" or "Bosnia and Herzegovina" or "Botswana" or "Bouvet Island" or "British Indian Ocean Territory" or "Brunei Darussalam" or "Bulgaria" or "Burkina Faso" or "Burundi" or c* or d* or e* or f* or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or r* or s* or t* or u* or v* or w* or x* or y* or z*) and subjarea(ENER)"""
    #rf entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(A* or B* or c* or d* or e* or "France" or "Finland" or "Fiji" or "French Polynesia" or "French Guiana" or "French Southern Territories" or "Falkland Islands" or "Faroe Islands" or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or "Reunion" or "Romania" or "Rwanda" or s* or t* or u* or v* or w* or x* or y* or z*) and subjarea(ENER)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""china"") and subjarea(ENER)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(A* or B* or c* or d* or e* or f* or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or r* or "Saint Helena" or "Saint Kitts and Nevis" or "Saint Lucia" or "Saint Pierre and Miquelon" or "Saint Vincent and the Grenadines" or "Samoa" or "San Marino" or "Sao Tome and Principe" or "Saudi Arabia" or "Senegal" or "Serbia" or "Seychelles" or "Sierra Leone" or "Singapore" or "Slovakia" or "Slovenia" or "Solomon Islands" or "Somalia" or "South Georgia and the South Sandwich Islands" or "South Korea" or "Spain" or "Sri Lanka" or "Sudan" or "Suriname" or "Svalbard and Jan Mayen" or "Swaziland" or "Sweden" or "Switzerland" or "Syrian Arab Republic" or t* or u* or v* or w* or x* or y* or z*)"""
    #entertext = u"""pubyear = 2014 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""" + countryname + """) and subjmain(""" + dicts_from_file[i].rstrip() + """)"""
    #entertext = u"""pubyear = 2003 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and subjmain(""" + dicts_from_file[i].rstrip() + """)"""
    entertext = u"""pubyear = 2014 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""" + countryname + """) and subjarea(""" + dicts_from_file[i].rstrip() + """)"""
    driver.find_element_by_id('searchfield').send_keys(entertext)#added str
    time.sleep(random.randrange(1,2))
    driver.find_element_by_id('advSearch').click()
    time.sleep(random.randrange(1,2))
    resulttext = driver.find_element_by_class_name('resultsCount').text
    with open("kozemir060317/" + "pub_" + filename + ".txt", "a") as myfile:
        myfile.write(countryname + "$" + dicts_from_file[i].rstrip() + "$" + (str(resulttext) + "\n").encode('utf-8'))
        #myfile.write(dicts_from_file[i].rstrip() + "$" + (str(resulttext) + "\n").encode('utf-8'))
    return;


for j in range(0,70):
    countryname = country_from_file[j].rstrip()
    for i in range(s,do):
        driver.get('http://www.scopus.com/search/form.uri?display=advanced&clear=t&origin=searchbasic&txGid=0')
        time.sleep(random.randrange(1,2))
        filename = ("subjarea_2014")
        #filename = (countryname + "_" + subjarea)
        try:
            gettothepageandsavetofile()
        except NoSuchElementException:
            with open("kozemir060317/" + "pub_" + filename  + ".txt", "a") as myfile:
                myfile.write((countryname + "$" + dicts_from_file[i].rstrip() + "$" + "no_data" + "\n").encode('utf-8'))
            print "no element"


#for i in range(s,do):
#    driver.get('http://www.scopus.com/search/form.uri?display=advanced&clear=t&origin=searchbasic&txGid=0')
#    time.sleep(random.randrange(1,2))
#    filename = ("subjarea_2003")
#    #filename = (countryname + "_" + subjarea)
#    try:
#        gettothepageandsavetofile()
#    except NoSuchElementException:
#        with open("kozemir060317/" + "pub_" + filename  + ".txt", "a") as myfile:
#            #myfile.write((countryname + "$" + dicts_from_file[i].rstrip() + "$" + "no_data" + "\n").encode('utf-8')) #for countries
#            myfile.write((dicts_from_file[i].rstrip() + "$" + "no_data" + "\n").encode('utf-8')) #without
#        print "no element"


print "___________________________________________________________________"
print "___________________________________________________________________"
print "done\n"
print "___________________________________________________________________"
driver.quit()
