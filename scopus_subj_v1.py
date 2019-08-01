# -*- coding: utf-8 -*-
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
from selenium.common.exceptions import NoSuchElementException

s = 0
do = 3

dicts_from_file = []
with open('scopus_list.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval('line'))

#file = open("WoS_WC/" + country + "_wc_" + dicts_from_file[i].rstrip() + "_" + str(i) + ".html","w")

for i in range(s,do):
    driver.get('http://www.scopus.com/search/form.uri?display=advanced&clear=t&origin=searchbasic&txGid=0')
    time.sleep(random.randrange(1,2))
    #entertext = "pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and SUBJMAIN(" + dicts_from_file[i].rstrip() + ") AND CU=(" + country + ")"
    entertext = "pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and SUBJMAIN(" + dicts_from_file[i].rstrip() + ")"
    driver.find_element_by_id('searchfield').send_keys(entertext)
    time.sleep(random.randrange(1,2))
    driver.find_element_by_css_selector('input.btnSearch.verticalAlignMiddle').click()
    time.sleep(random.randrange(1,2))
    resulttext = driver.find_element_by_class_name('resultsCount').text
    file = open("WoS_WC/world.txt","w")
    file.write(str(resulttext))
    time.sleep(random.randrange(1,2))
    file.close()
