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
do = 2#333

#filename = "Intra_brics_collab"
#filename = "brics_upd"
#filename = "Russia_and_brics"
#filename = "Russia_and_SouthAfrica"
#filename = "China_and_South Africa"
filename = "test_energy"

subjarea ="ENER"
country = "'Russian Federation'"
#dicts_from_file = []
#with open('scopus_list.txt','r') as inf:
#    for line in inf:
#        dicts_from_file.append(eval('line'))

names_from_file = []
with open('scopus_subj_names.txt','r') as inf:
    for line in inf:
        names_from_file.append(eval('line'))

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
        #entertext = u"""PUBYEAR  <  2016  AND  PUBYEAR  >  2010  AND  ( DOCTYPE ( ar )  OR  DOCTYPE ( cp )  OR  DOCTYPE ( re ) )  AND  AFFILCOUNTRY ( south  africa  AND  ( "United States"  OR  "Russian Federation"  OR  "United Kingdom"  OR  "Germany"  OR  "Japan"  OR  "France"  OR  "Canada"  OR  "Italy"  OR  "China"  OR  "Spain"  OR  "Australia"  OR  "South Korea"  OR  "Netherlands"  OR  "India"  OR  "Switzerland"  OR  "Taiwan"  OR  "Sweden"  OR  "Poland"  OR  "Turkey"  OR  "Belgium"  OR  "Iran"  OR  "Israel"  OR  "Austria"  OR  "Denmark"  OR  "Finland"  OR  "Greece"  OR  "Czech Republic"  OR  "Mexico"  OR  "Norway"  OR  "Hong Kong"  OR  "Singapore"  OR  "Portugal"  OR  "Brazil"  OR  "Malaysia"  OR  "New Zealand"  OR  "Argentina"  OR  "Ireland"  OR  "Hungary"  OR  "Ukraine"  OR  "Romania"  OR  "Egypt"  OR  "Thailand"  OR  "Saudi Arabia"  OR  "Chile"  OR  "Pakistan"  OR  "Slovakia"  OR  "Croatia"  OR  "Slovenia"  OR  "Colombia"  OR  "Bulgaria"  OR  "Nigeria"  OR  "Tunisia"  OR  "Serbia"  OR  "Algeria"  OR  "Morocco"  OR  "Indonesia"  OR  "Lithuania"  OR  "Venezuela"  OR  "Cuba"  OR  "United Arab Emirates"  OR  "Belarus"  OR  "Bangladesh"  OR  "Viet Nam"  OR  "Estonia"  OR  "Jordan"  OR  "Kenya"  OR  "Lebanon"  OR  "Philippines"  OR  "Kuwait"  OR  "Cyprus"  OR  "Latvia"  OR  "Iceland"  OR  "Peru"  OR  "Puerto Rico"  OR  "Uruguay"  OR  "Qatar"  OR  "Ethiopia"  OR  "Armenia"  OR  "Oman"  OR  "Luxembourg"  OR  "Sri Lanka"  OR  "Kazakhstan"  OR  "Tanzania"  OR  "Iraq"  OR  "Ghana"  OR  "Uganda"  OR  "Georgia"  OR  "Cameroon"  OR  "Azerbaijan"  OR  "Uzbekistan"  OR  "Costa Rica"  OR  "Nepal"  OR  "Macedonia"  OR  "Ecuador"  OR  "Zimbabwe"  OR  "Senegal"  OR  "Bosnia and Herzegovina"  OR  "Sudan"  OR  "Moldova"  OR  "Syrian Arab Republic"  OR  "Macao"  OR  "Panama"  OR  "Botswana"  OR  "Trinidad and Tobago"  OR  "Malawi"  OR  "Côte d'Ivoire"  OR  "Burkina Faso"  OR  "Jamaica"  OR  "Bahrain"  OR  "Palestine"  OR  "Malta"  OR  "Libya"  OR  "Zambia"  OR  "Benin"  OR  "Bolivia"  OR  "Mongolia"  OR  "Congo"  OR  "Madagascar"  OR  "Albania"  OR  "Yemen"  OR  "Cambodia"  OR  "Mali"  OR  "Brunei Darussalam"  OR  "Fiji"  OR  "North Korea"  OR  "Mozambique"  OR  "Namibia"  OR  "Guatemala"  OR  "Papua New Guinea"  OR  "Montenegro"  OR  "Mauritius"  OR  "New Caledonia"  OR  "Gabon"  OR  "Gambia"  OR  "Laos"  OR  "Rwanda"  OR  "Barbados"  OR  "Niger"  OR  "Monaco"  OR  "Myanmar"  OR  "Kyrgyzstan"  OR  "Togo"  OR  "Paraguay"  OR  "Guadeloupe"  OR  "Nicaragua"  OR  "French Polynesia"  OR  "Liechtenstein"  OR  "Tajikistan"  OR  "El Salvador"  OR  "Dominican Republic"  OR  "Swaziland"  OR  "Honduras"  OR  "Greenland"  OR  "Grenada"  OR  "French Guiana"  OR  "Afghanistan"  OR  "Guam"  OR  "Haïti"  OR  "Angola"  OR  "Martinique"  OR  "Bermuda"  OR  "Guinea"  OR  "Sierra Leone"  OR  "Reunion"  OR  "Bhutan"  OR  "Central African Republic"  OR  "Guyana"  OR  "Democratic Republic Congo"  OR  "Faroe Islands"  OR  "Eritrea"  OR  "Seychelles"  OR  "Mauritania"  OR  "Lesotho"  OR  "Guinea-Bissau"  OR  "Netherlands Antilles"  OR  "Burundi"  OR  "Bahamas"  OR  "Chad"  OR  "Falkland Islands (Malvinas)"  OR  "Saint Kitts and Nevis"  OR  "Belize"  OR  "Solomon Islands"  OR  "Vanuatu"  OR  "Turkmenistan"  OR  "Suriname"  OR  "Dominica"  OR  "Liberia"  OR  "Samoa"  OR  "Cayman Islands"  OR  "Virgin Islands (U.S.)"  OR  "Maldives"  OR  "Cape Verde"  OR  "San Marino"  OR  "Djibouti"  OR  "Federated States of Micronesia"  OR  "Andorra"  OR  "American Samoa"  OR  "Equatorial Guinea"  OR  "Palau"  OR  "Timor-Leste"  OR  "Virgin Islands (British)"  OR  "Somalia"  OR  "Antigua and Barbuda"  OR  "Tonga"  OR  "Gibraltar"  OR  "Saint Lucia"  OR  "Comoros"  OR  "Montserrat"  OR  "Aruba"  OR  "Marshall Islands"  OR  "Mayotte"  OR  "Northern Mariana Islands"  OR  "Cook Islands"  OR  "Sao Tome and Principe"  OR  "Turks and Caicos Islands"  OR  "Saint Vincent and the Grenadines"  OR  "Anguilla"  OR  "Kiribati"  OR  "United States Minor Outlying Islands"  OR  "Tuvalu"  OR  "Vatican City State"  OR  "Nauru"  OR  "Norfolk Island"  OR  "Svalbard and Jan Mayen"  OR  "British Indian Ocean Territory"  OR  "Niue"  OR  "Wallis and Futuna"  OR  "Saint Helena"  OR  "Cocos (Keeling) Islands"  OR  "Western Sahara"  OR  "Christmas Island"  OR  "South Georgia and the South Sandwich Islands"  OR  "Bouvet Island"  OR  "Saint Pierre and Miquelon"  OR  "French Southern Territories"  OR  "Pitcairn"  OR  "Tokelau"  OR  "Heard Island and McDonald Islands" ) ) and SUBJMAIN(""" + dicts_from_file[i].rstrip() + """)"""
        entertext = u"""pubyear > 2010 and pubyear < 2016 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry(""" + country + """) and subjarea(ENER)"""
        #time.sleep(random.randrange(1,3))
        driver.find_element_by_id('searchfield').send_keys(entertext)#added str
        time.sleep(random.randrange(1,2))
        #driver.find_element_by_css_selector('input.btnSearch.verticalAlignMiddle').click()
        driver.find_element_by_id('advSearch').click()
        time.sleep(random.randrange(1,2))
        resulttext = driver.find_element_by_class_name('resultsCount').text
        afil = driver.find_element_by_id('searchResFormId').text
#        csv = driver.find_element_by_name('exportRefine').click()
        analyzeres = driver.find_element_by_class_name('citationOverview').click()
#        afiltab = driver.find_element_by_id('aaffilTab').click()
        #afiltable = driver.find_element_by_xpath("//div[@class='analyzerHeader']").text
#        afiltable = driver.find_element_by_xpath("//label[@id='label60021331']").text #//label[@class='']
        #afil_test2 = driver.find_element_by_xpath("//td[2][@class='sorting_1']").text
    #    driver.location_once_scrolled_into_view("id='jsonMainResponse'")
        afil_test2 = driver.find_element_by_xpath("//div[@class='analyzer']")
        time.sleep(random.randrange(1,2))

#        afil_test2 = driver.find_element_by_id('jsonMainResponse').text
        #afiltable = driver.find_element_by_link_text('/affil/profile.uri?afid=60021331&origin=resultsAnalyzer&zone=affiliationName').text
        #("/html/body/form/div[@id='firstLvlTabs']/div[@class='tabFunc']/div[@id='lvl1Tab3']/div[@id='affilChartTable']/div[@class='dataItems']/div[@id='affilTableDiv']/div[@id='affilTable_wrapper']/").text
        #driver.find_element_by_class_name('odd').text
#        for l in range(0,3):
#            print(afil_test2[l])


    #    print str(resulttext)
#        print str(afiltable)
        #print afil_test2.get_attribute('innerHTML')
        #print afil_test2.get_attribute('textContent')
        newtest = driver.execute_script("return arguments[0].innerHTML", afil_test2)
        print newtest.encode("utf-8")
        #afil = driver.find_element_by_class_name('textCol').text
        with open("Scopus/" + filename + ".txt", "a") as myfile:
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
