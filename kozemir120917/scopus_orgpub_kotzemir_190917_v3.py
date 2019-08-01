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

#берет номер организации из файла, подставляет в запрос, забирает количество публикаци, записывает в файл (номер_организации$кол_запросов)
country = "sa"
countryname = country + "-brics"
#subjarea = "subjarea(ENER)"

dicts_from_file = []
with open('org_scopus/org_' + country + '.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval('line'))

s = 0
num_lines = sum(1 for line in open('org_scopus/org_' + country + '.txt'))
do = num_lines#160
#do = 29#160

def gettothepageandsavetofile():
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""Russian Federation"") and subjarea(ENER)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry( A* or B* or c* or d* or e* or f* or g* or h* or "Iceland" or "Indonesia" or "Iran" or "Iraq" or "Ireland"or "Israel"or "Italy" or j* or k* or l* or m* or n* or o* or p* or q* or r* or s* or t* or u* or v* or w* or x* or y* or z*) and subjarea(ENER)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""Russian Federation"") and subjarea(ENER)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry( A* or "Bahamas" or "Bahrain" or "Bangladesh" or "Barbados" or "Belarus" or "Belgium" or "Belize" or "Benin" or "Bermuda" or "Bhutan" or "Bolivia" or "Bosnia and Herzegovina" or "Botswana" or "Bouvet Island" or "British Indian Ocean Territory" or "Brunei Darussalam" or "Bulgaria" or "Burkina Faso" or "Burundi" or c* or d* or e* or f* or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or r* or s* or t* or u* or v* or w* or x* or y* or z*) and subjarea(ENER)"""
    #rf entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(A* or B* or c* or d* or e* or "France" or "Finland" or "Fiji" or "French Polynesia" or "French Guiana" or "French Southern Territories" or "Falkland Islands" or "Faroe Islands" or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or "Reunion" or "Romania" or "Rwanda" or s* or t* or u* or v* or w* or x* or y* or z*) and subjarea(ENER)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""china"") and subjarea(ENER)"""
#    entertext = u"""pubyear > 2010 and pubyear < 2016 and """ + dicts_from_file[i].rstrip() + """ and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re))"""
#total    entertext = u"""af-ID(""" + dicts_from_file[i].rstrip() + """) and (DOCTYPE(ar or cp or re) and pubyear > 2009 and pubyear < 2017)"""
#world    entertext = u"""af-ID(""" + dicts_from_file[i].rstrip() + """) and (DOCTYPE(ar or cp or re) and AFFILCOUNTRY (A* or "Bahamas" or "Bahrain" or "Bangladesh" or "Barbados" or "Belarus" or "Belgium" or "Belize" or "Benin" or "Bermuda" or "Bhutan" or "Bolivia" or "Bosnia and Herzegovina" or "Botswana" or "Bouvet Island" or "British Indian Ocean Territory" or "Brunei Darussalam" or "Bulgaria" or "Burkina Faso" or "Burundi" or c* or d* or e* or f* or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or r* or s* or t* or u* or v* or w* or x* or y* or z*)  and pubyear > 2009 and pubyear < 2017 and   (SUBJMAIN(2102) or SUBJMAIN(2103)))"""
    #mir entertext = u"""af-ID(""" + dicts_from_file[i].rstrip() + """) and (DOCTYPE(ar OR cp OR re)) and AFFILCOUNTRY(A* or B* or c* or d* or e* or "Falkland Islands (Malvinas)" or "Faroe Islands" or "Federated States of Micronesia" or "Fiji" or "Finland" or "France" or "French Guiana" or "French Polynesia" or "French Southern Territories"  or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or "Reunion" or "Romania" or "Rwanda" or s* or t* or u* or v* or w* or x* or y* or z*)  and pubyear > 2009 and pubyear < 2017 and (SUBJMAIN(2102) or SUBJMAIN(2103))"""
    #rf entertext = u"""af-ID(""" + dicts_from_file[i].rstrip() + """) and (DOCTYPE(ar OR cp OR re)) and AFFILCOUNTRY(Brazil or India or China or "South Africa")  and pubyear > 2009 and pubyear < 2017 and (SUBJMAIN(2102) or SUBJMAIN(2103))"""
    entertext = u"""af-ID(""" + dicts_from_file[i].rstrip() + """) and (DOCTYPE(ar OR cp OR re)) and AFFILCOUNTRY("Russian Federation" or Brazil or India or China)  and pubyear > 2009 and pubyear < 2017 and (SUBJMAIN(2102) or SUBJMAIN(2103))"""

    driver.find_element_by_id('searchfield').send_keys(entertext)#added str
    time.sleep(random.randrange(1,2))
    driver.find_element_by_id('advSearch').click()
    time.sleep(random.randrange(1,2))
    resulttext = driver.find_element_by_class_name('resultsCount').text
    with open("org_output/" + filename + "_org.txt", "a") as myfile:
        myfile.write(dicts_from_file[i].rstrip() + "$" + (str(resulttext) + "\n").encode('utf-8'))
    return;



for i in range(s,do):
    driver.get('http://www.scopus.com/search/form.uri?display=advanced&clear=t&origin=searchbasic&txGid=0')
    time.sleep(random.randrange(1,2))
    filename = (countryname)
    #filename = (countryname + "_" + subjarea)
    try:
        gettothepageandsavetofile()
    except NoSuchElementException:
        with open("org_output/" + filename  + "_org.txt", "a") as myfile:
            myfile.write((dicts_from_file[i].rstrip() + "$" + "no_data" + "\n").encode('utf-8'))
        print "no element"

print "___________________________________________________________________"
print "___________________________________________________________________"
print "done\n"
print "___________________________________________________________________"
driver.quit()
