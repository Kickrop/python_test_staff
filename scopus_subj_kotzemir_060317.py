# -*- coding: utf-8 -*-
import time
import random
import json
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
#driver = webdriver.FireFox("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
from selenium.common.exceptions import NoSuchElementException

s = 0
do = 5#333

#filename = "Intra_brics_collab"
#filename = "brics_upd"
#filename = "Russia_and_brics"
#filename = "Russia_and_SouthAfrica"
#filename = "China_and_South Africa"


subjarea ="big"
country = "Australia"
filename = (country)
dicts_from_file = []
with open('scopus_subj_names_big.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval('line'))

#names_from_file = []
#with open('scopus_subj_names_test_ener.txt','r') as inf:
#    for line in inf:
#        names_from_file.append(eval('line'))

#file = open("WoS_WC/" + country + "_wc_" + dicts_from_file[i].rstrip() + "_" + str(i) + ".html","w")

for i in range(s,do):
    driver.get('http://www.scopus.com/search/form.uri?display=advanced&clear=t&origin=searchbasic&txGid=0')
    time.sleep(random.randrange(1,2))
    try:
        #entertext = "pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and SUBJMAIN(" + dicts_from_file[i].rstrip() + ") AND CU=(" + country + ")"
        #world #entertext = "pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and SUBJMAIN(" + dicts_from_file[i].rstrip() + ")"
        #brics_upd entertext = 'pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and AFFILCOUNTRY ("russian federation" or "china" or "india" or "brazil" or "south africa") and SUBJMAIN(' + dicts_from_file[i].rstrip() + ')'
        #Intra_brics_collab entertext = "(pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and AFFILCOUNTRY ((russian federation AND china) or (russian federation AND India) or (russian federation AND Brazil) or (russian federation AND south africa) or ( China AND India) or (china AND Brazil) or (China AND South Africa) or (India AND Brazil) or (India AND South Africa) or (Brazil AND South Africa)) and SUBJMAIN(" + dicts_from_file[i].rstrip() + "))"
        #russia entertext = "pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and AFFILCOUNTRY ( ( russian  federation  AND china) or (russian fedration and india) or (russian federation and brazil) or (russian federation and south Africa))"" and SUBJMAIN(' + dicts_from_file[i].rstrip() + ")"
        #russia and brics entertext = "PUBYEAR < 2016  AND  PUBYEAR > 2010 AND (DOCTYPE (ar) OR DOCTYPE (cp) OR DOCTYPE (re)) AND AFFILCOUNTRY ((russian federation  AND  china) OR (russian fedration AND india) OR (russian federation AND brazil )  OR  ( russian  federation  AND  south  africa )) and SUBJMAIN(" + dicts_from_file[i].rstrip() + ")"
        #russia and china entertext = "pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and AFFILCOUNTRY ( russian  federation  AND china) and SUBJMAIN(" + dicts_from_file[i].rstrip() + ")"
        #entertext = "pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and AFFILCOUNTRY (South Africa) and SUBJMAIN(" + dicts_from_file[i].rstrip() + ")"
        #china and brics entertext = "pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and AFFILCOUNTRY ((russian federation AND china) or (China and india) or (China and brazil) or (China and south Africa)) and SUBJMAIN(" + dicts_from_file[i].rstrip() + ")"
        #china and country entertext = "pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and AFFILCOUNTRY (China AND South Africa) and SUBJMAIN(" + dicts_from_file[i].rstrip() + ")"
        #entertext = u"""PUBYEAR  <  2016  AND  PUBYEAR  >  2010  AND  ( DOCTYPE ( ar )  OR  DOCTYPE ( cp )  OR  DOCTYPE ( re ) )  AND  AFFILCOUNTRY ( south  africa  AND  ( "United States"  OR  "Russian Federation"  OR  "United Kingdom"  OR  "Germany"  OR  "Japan"  OR  "France"  OR  "Canada"  OR  "Italy"  OR  "China"  OR  "Spain"  OR  "Australia"  OR  "South Korea"  OR  "Netherlands"  OR  "India"  OR  "Switzerland"  OR  "Taiwan"  OR  "Sweden"  OR  "Poland"  OR  "Turkey"  OR  "Belgium"  OR  "Iran"  OR  "Israel"  OR  "Austria"  OR  "Denmark"  OR  "Finland"  OR  "Greece"  OR  "Czech Republic"  OR  "Mexico"  OR  "Norway"  OR  "Hong Kong"  OR  "Singapore"  OR  "Portugal"  OR  "Brazil"  OR  "Malaysia"  OR  "New Zealand"  OR  "Argentina"  OR  "Ireland"  OR  "Hungary"  OR  "Ukraine"  OR  "Romania"  OR  "Egypt"  OR  "Thailand"  OR  "Saudi Arabia"  OR  "Chile"  OR  "Pakistan"  OR  "Slovakia"  OR  "Croatia"  OR  "Slovenia"  OR  "Colombia"  OR  "Bulgaria"  OR  "Nigeria"  OR  "Tunisia"  OR  "Serbia"
        entertext = u"""pubyear = 2003 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry("Australia") and subjmain(""" + dicts_from_file[i].rstrip() + """)"""
        #time.sleep(random.randrange(1,3))
        driver.find_element_by_id('searchfield').send_keys(entertext)#added str
        time.sleep(random.randrange(1,2))
        driver.find_element_by_id('advSearch').click()
        time.sleep(random.randrange(1,2))
        resulttext = driver.find_element_by_class_name('resultsCount').text
        afil = driver.find_element_by_id('searchResFormId').text
        analyzeres = driver.find_element_by_class_name('citationOverview').click()

        afil_test2 = driver.find_element_by_xpath("//pre[@id='jsonMainResponse']")
        time.sleep(random.randrange(1,2))

        newtest = driver.execute_script("return arguments[0].textContent", afil_test2)

    #    pam = dicts_from_file[i]
    #    pam1 = pam.split('\n')
    #    print newtest.encode("utf-8")
        #afil = driver.find_element_by_class_name('textCol').text
        with open("kozemir060317/" + "JSON_"+ filename + "_test_" + str(i) + "_.txt", "w") as myfile:
        #print str(afil)
            myfile.write(newtest.encode("utf-8"))
    except NoSuchElementException:
#        with open("Scopus/" + filename + ".txt", "a") as myfile:
#            myfile.write(str(i) + ";" + country + ";" + subjarea + ";" + "0" + "\n")
#        time.sleep(random.randrange(1,2))
        print "no element"

print "___________________________________________________________________"
print "___________________________________________________________________"
print "done\n"
print "___________________________________________________________________"
