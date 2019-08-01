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
#webdriver_service = service.Service("C:\Program Files\Opera")
#webdriver_service.start()
#driver = webdriver.Opera("C:\Program Files\Opera\operadriver.exe")
#driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

#driver = webdriver.Firefox()
#driver = webdriver.FireFox("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
from selenium.common.exceptions import NoSuchElementException

s = 0
do = 1#333

#filename = "Intra_brics_collab"
#filename = "brics_upd"
#filename = "Russia_and_brics"
#filename = "Russia_and_SouthAfrica"
#filename = "China_and_South Africa"


#subjarea ="ENER"
countryname = "Australia"
subjarea = "subjarea(ENER)"
dicts_from_file = []
with open('scopus_subj_names_big.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval('line'))
#dicts_from_file = []
#with open('scopus_subj_names_test_ener.txt','r') as inf:
#    for line in inf:
#        dicts_from_file.append(eval('line'))


#names_from_file = []
#with open('scopus_subj_names_test_ener.txt','r') as inf:
#    for line in inf:
#        names_from_file.append(eval('line'))

#file = open("WoS_WC/" + country + "_wc_" + dicts_from_file[i].rstrip() + "_" + str(i) + ".html","w")
def gettothepageandsavetofile():
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""Russian Federation"" and ""China"") and """ + subjarea
    entertext = u"""pubyear = 2003 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry("Australia") and subjmain(""" + dicts_from_file[i].rstrip() + """)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""Russian Federation"" and (A* or B* or c* or d* or e* or f* or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or "Reunion" or "Romania" or "Rwanda" or s* or t* or u* or v* or w* or x* or y* or z*)) and subjmain(""" + dicts_from_file[i].rstrip() + """)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry( South Africa and (A* or B* or c* or d* or e* or f* or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or r* or "Saint Helena" or "Saint Kitts and Nevis" or "Saint Lucia" or "Saint Pierre and Miquelon" or "Saint Vincent and the Grenadines" or "Samoa" or "San Marino" or "Sao Tome and Principe" or "Saudi Arabia" or "Senegal" or "Serbia" or "Seychelles" or "Sierra Leone" or "Singapore" or "Slovakia" or "Slovenia" or "Solomon Islands" or "Somalia" or "South Georgia and the South Sandwich Islands" or "South Korea" or "Spain" or "Sri Lanka" or "Sudan" or "Suriname" or "Svalbard and Jan Mayen" or "Swaziland" or "Sweden" or "Switzerland" or "Syrian Arab Republic" or t* or u* or v* or w* or x* or y* or z*)) and subjmain(""" + dicts_from_file[i].rstrip() + """)"""
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""South Africa"" and ("Afghanistan" or "Albania" or "Algeria" or "American Samoa" or "Andorra" or "Angola" or "Anguilla" or "Antarctica" or "Antigua and Barbuda" or "Argentina" or "Armenia" or "Aruba" or "Australia" or "Austria" or "Azerbaijan" or B* or c* or d* or e* or f* or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or r* or "Saint Helena" or "Saint Kitts and Nevis" or "Saint Lucia" or "Saint Pierre and Miquelon" or "Saint Vincent and the Grenadines" or "Samoa" or "San Marino" or "Sao Tome and Principe" or "Saudi Arabia" or "Senegal" or "Serbia" or "Seychelles" or "Sierra Leone" or "Singapore" or "Slovakia" or "Slovenia" or "Solomon Islands" or "Somalia" or "South Georgia and the South Sandwich Islands" or "South Korea" or "Spain" or "Sri Lanka" or "Sudan" or "Suriname" or "Svalbard and Jan Mayen" or "Swaziland" or "Sweden" or "Switzerland" or "Syrian Arab Republic" or t* or u* or v* or w* or x* or y* or z*))""" + subjarea
    #entertext = u"""pubyear > 2010 and pubyear < 2016 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry( “Brazil” and (A* or "Bahamas" or "Bahrain" or "Bangladesh" or "Barbados" or "Belarus" or "Belgium" or "Belize" or "Benin" or "Bermuda" or "Bhutan" or "Bolivia" or "Bosnia and Herzegovina" or "Botswana" or "Bouvet Island" or "British Indian Ocean Territory" or "Brunei Darussalam" or "Bulgaria" or "Burkina Faso" or "Burundi" or c* or d* or e* or f* or g* or h* or i* or j* or k* or l* or m* or n* or o* or p* or q* or r* or s* or t* or u* or v* or w* or x* or y* or z*)) and """ + subjarea
#time.sleep(random.randrange(1,3))
    driver.find_element_by_id('searchfield').send_keys(entertext)#added str

#    def sendkeys():
#        for j in range(len(entertext)):
#            driver.find_element_by_id('searchfield').send_keys(entertext[j])
#        return
#    sendkeys()
    #pam = driver.find_element_by_id('searchfield').value = entertext
    #driver.execute_script("return arguments[0].value = arguments[1]", pam)
#    inputField = driver.find_element_by_id('searchfield')
#    driver.execute_script("arguments[0].setAttribute('value', arguments[1])", inputField, entertext)
    time.sleep(random.randrange(1,2))
    driver.find_element_by_id('advSearch').click()
    time.sleep(random.randrange(1,2))
    resulttext = driver.find_element_by_class_name('resultsCount').text
    #afil = driver.find_element_by_id('searchResFormId').text
    analyzeres = driver.find_element_by_class_name('citationOverview').click()

    afil_test2 = driver.find_element_by_xpath("//pre[@id='jsonMainResponse']")
    time.sleep(random.randrange(1,2))
    getjson = driver.execute_script("return arguments[0].textContent", afil_test2)
    with open("kozemir120917/" + "JSON_"+ filename + "_" + str(i) + ".txt", "w") as myfile:
    #print str(afil)
        myfile.write(getjson.encode("utf-8"))
        #        with open("Scopus/" + filename + ".txt", "a") as myfile:
        #            myfile.write(str(i) + ";" + country + ";" + subjarea + ";" + "0" + "\n")
        #        time.sleep(random.randrange(1,2))
    return;



for i in range(s,do):
    driver.get('http://www.scopus.com/search/form.uri?display=advanced&clear=t&origin=searchbasic&txGid=0')
    time.sleep(random.randrange(1,2))
    #filename = (countryname + "_" + dicts_from_file[i].rstrip())
    filename = (countryname + "_" + subjarea)
    try:
        gettothepageandsavetofile()
    except NoSuchElementException:
        print "no element"

print "___________________________________________________________________"
print "___________________________________________________________________"
print "done\n"
print "___________________________________________________________________"
driver.quit()
