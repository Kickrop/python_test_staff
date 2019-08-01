# -*- coding: utf-8 -*-
import json
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

entertext = u"""pubyear > 2010 and pubyear < 2016 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and affilcountry("Russi"""
driver.get('http://www.scopus.com/search/form.uri?display=advanced&clear=t&origin=searchbasic&txGid=0')

driver.find_element_by_id('contentEditLabel').click()
inputField = driver.find_element_by_id('contentEditLabel')
driver.execute_script("arguments[0].setAttribute('value', arguments[1])", inputField, entertext)
#dicts_from_file = []
#with open('scopus_subj_names_test_ener.txt','r') as inf:
#    for line in inf:
#        dicts_from_file.append(eval('line'))
#print dicts_from_file[0]
#with open("kozemir070217/" + "JSON" + dicts_from_file[0] + ".txt", "w") as myfile:
#print str(afil)
#    myfile.write(str(dicts_from_file[0]))
dicts_from_file = ['2001', '3201']
#print entertext.encode("utf-8")

#driver.quit()
