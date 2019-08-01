# -*- coding: utf-8 -*-
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

filename = "output_affil_address"


dicts_from_file = []
with open('affil_id.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval('line'))

#names_from_file = []
#with open('scopus_subj_names.txt','r') as inf:
#    for line in inf:
#        names_from_file.append(eval('line'))

s = 46880
do = len(dicts_from_file)#333

#file = open("WoS_WC/" + country + "_wc_" + dicts_from_file[i].rstrip() + "_" + str(i) + ".html","w")

for i in range(s,do):
    #driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS)
    driver.get('https://www.scopus.com/affil/profile.uri?afid=' + dicts_from_file[i] + '&origin=resultsAnalyzer&zone=affiliationName')
    #time.sleep(random.randrange(3,4))
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "profileleftinside")))
        #entertext = u"""PUBYEAR  <  2016  AND  PUBYEAR  >  2010  AND  ( DOCTYPE ( ar )  OR  DOCTYPE ( cp )  OR  DOCTYPE ( re ) )  AND  AFFILCOUNTRY ( south  africa  AND  ( "United States"  OR  "Russian Federation"  OR  "United Kingdom"  OR  "Germany"  OR  "Japan"  OR  "France"  OR  "Canada"  OR  "Italy"  OR  "China"  OR  "Spain"  OR  "Australia"  OR  "South Korea"  OR  "Netherlands"  OR  "India"  OR  "Switzerland"  OR  "Taiwan"  OR  "Sweden"  OR  "Poland"  OR  "Turkey"  OR  "Belgium"  OR  "Iran"  OR  "Israel"  OR  "Austria"  OR  "Denmark"  OR  "Finland"  OR  "Greece"  OR  "Czech Republic"  OR  "Mexico"  OR  "Norway"  OR  "Hong Kong"  OR  "Singapore"  OR  "Portugal"  OR  "Brazil"  OR  "Malaysia"  OR  "New Zealand"  OR  "Argentina"  OR  "Ireland"  OR  "Hungary"  OR  "Ukraine"  OR  "Romania"  OR  "Egypt"  OR  "Thailand"  OR  "Saudi Arabia"  OR  "Chile"  OR  "Pakistan"  OR  "Slovakia"  OR  "Croatia"  OR  "Slovenia"  OR  "Colombia"  OR  "Bulgaria"  OR  "Nigeria"  OR  "Tunisia"  OR  "Serbia"  OR  "Algeria"  OR  "Morocco"  OR  "Indonesia"  OR  "Lithuania"  OR  "Venezuela"  OR  "Cuba"  OR  "United Arab Emirates"  OR  "Belarus"  OR  "Bangladesh"  OR  "Viet Nam"  OR  "Estonia"  OR  "Jordan"  OR  "Kenya"  OR  "Lebanon"  OR  "Philippines"  OR  "Kuwait"  OR  "Cyprus"  OR  "Latvia"  OR  "Iceland"  OR  "Peru"  OR  "Puerto Rico"  OR  "Uruguay"  OR  "Qatar"  OR  "Ethiopia"  OR  "Armenia"  OR  "Oman"  OR  "Luxembourg"  OR  "Sri Lanka"  OR  "Kazakhstan"  OR  "Tanzania"  OR  "Iraq"  OR  "Ghana"  OR  "Uganda"  OR  "Georgia"  OR  "Cameroon"  OR  "Azerbaijan"  OR  "Uzbekistan"  OR  "Costa Rica"  OR  "Nepal"  OR  "Macedonia"  OR  "Ecuador"  OR  "Zimbabwe"  OR  "Senegal"  OR  "Bosnia and Herzegovina"  OR  "Sudan"  OR  "Moldova"  OR  "Syrian Arab Republic"  OR  "Macao"  OR  "Panama"  OR  "Botswana"  OR  "Trinidad and Tobago"  OR  "Malawi"  OR  "Côte d'Ivoire"  OR  "Burkina Faso"  OR  "Jamaica"  OR  "Bahrain"  OR  "Palestine"  OR  "Malta"  OR  "Libya"  OR  "Zambia"  OR  "Benin"  OR  "Bolivia"  OR  "Mongolia"  OR  "Congo"  OR  "Madagascar"  OR  "Albania"  OR  "Yemen"  OR  "Cambodia"  OR  "Mali"  OR  "Brunei Darussalam"  OR  "Fiji"  OR  "North Korea"  OR  "Mozambique"  OR  "Namibia"  OR  "Guatemala"  OR  "Papua New Guinea"  OR  "Montenegro"  OR  "Mauritius"  OR  "New Caledonia"  OR  "Gabon"  OR  "Gambia"  OR  "Laos"  OR  "Rwanda"  OR  "Barbados"  OR  "Niger"  OR  "Monaco"  OR  "Myanmar"  OR  "Kyrgyzstan"  OR  "Togo"  OR  "Paraguay"  OR  "Guadeloupe"  OR  "Nicaragua"  OR  "French Polynesia"  OR  "Liechtenstein"  OR  "Tajikistan"  OR  "El Salvador"  OR  "Dominican Republic"  OR  "Swaziland"  OR  "Honduras"  OR  "Greenland"  OR  "Grenada"  OR  "French Guiana"  OR  "Afghanistan"  OR  "Guam"  OR  "Haïti"  OR  "Angola"  OR  "Martinique"  OR  "Bermuda"  OR  "Guinea"  OR  "Sierra Leone"  OR  "Reunion"  OR  "Bhutan"  OR  "Central African Republic"  OR  "Guyana"  OR  "Democratic Republic Congo"  OR  "Faroe Islands"  OR  "Eritrea"  OR  "Seychelles"  OR  "Mauritania"  OR  "Lesotho"  OR  "Guinea-Bissau"  OR  "Netherlands Antilles"  OR  "Burundi"  OR  "Bahamas"  OR  "Chad"  OR  "Falkland Islands (Malvinas)"  OR  "Saint Kitts and Nevis"  OR  "Belize"  OR  "Solomon Islands"  OR  "Vanuatu"  OR  "Turkmenistan"  OR  "Suriname"  OR  "Dominica"  OR  "Liberia"  OR  "Samoa"  OR  "Cayman Islands"  OR  "Virgin Islands (U.S.)"  OR  "Maldives"  OR  "Cape Verde"  OR  "San Marino"  OR  "Djibouti"  OR  "Federated States of Micronesia"  OR  "Andorra"  OR  "American Samoa"  OR  "Equatorial Guinea"  OR  "Palau"  OR  "Timor-Leste"  OR  "Virgin Islands (British)"  OR  "Somalia"  OR  "Antigua and Barbuda"  OR  "Tonga"  OR  "Gibraltar"  OR  "Saint Lucia"  OR  "Comoros"  OR  "Montserrat"  OR  "Aruba"  OR  "Marshall Islands"  OR  "Mayotte"  OR  "Northern Mariana Islands"  OR  "Cook Islands"  OR  "Sao Tome and Principe"  OR  "Turks and Caicos Islands"  OR  "Saint Vincent and the Grenadines"  OR  "Anguilla"  OR  "Kiribati"  OR  "United States Minor Outlying Islands"  OR  "Tuvalu"  OR  "Vatican City State"  OR  "Nauru"  OR  "Norfolk Island"  OR  "Svalbard and Jan Mayen"  OR  "British Indian Ocean Territory"  OR  "Niue"  OR  "Wallis and Futuna"  OR  "Saint Helena"  OR  "Cocos (Keeling) Islands"  OR  "Western Sahara"  OR  "Christmas Island"  OR  "South Georgia and the South Sandwich Islands"  OR  "Bouvet Island"  OR  "Saint Pierre and Miquelon"  OR  "French Southern Territories"  OR  "Pitcairn"  OR  "Tokelau"  OR  "Heard Island and McDonald Islands" ) ) and SUBJMAIN(""" + dicts_from_file[i].rstrip() + """)"""
        #time.sleep(random.randrange(1,3))
        #driver.find_element_by_id('searchfield').send_keys(entertext)
        affilState = driver.find_element_by_class_name('affilAddressState').text
        affilStreet = driver.find_element_by_class_name('affilAddressStreet').text
        affilId = dicts_from_file[i]
        #print affilState + "\n" + affilStreet + "\n" + affilId + "\n"
        time.sleep(random.randrange(2,3))
        with open(filename + ".txt", "a") as myfile:
            #myfile.write(str(i) + ";" + names_from_file[i].rstrip() + ";" + dicts_from_file[i].rstrip() + ";" + resulttext + "\n")
            myfile.write((str(i) + "$" + affilState + "$" + affilStreet + "$" + str(affilId)).encode('utf-8'))
    except (NoSuchElementException,  TimeoutException):
        #TimeoutException
        #with open("Scopus/" + filename + ".txt", "a") as myfile:
        #    myfile.write((str(i) + "$" + "$" + "$" + str(affilId)).encode('utf-8'))
        #time.sleep(random.randrange(1,2))
        print "not found" + str(i)
    #finally:
    #    driver.quit()
print "___________________________________________________________________"
print "done\n"
print "___________________________________________________________________"
