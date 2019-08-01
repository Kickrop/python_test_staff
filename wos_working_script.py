# -*- coding: utf-8 -*-

import time
import random
from selenium import webdriver
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

#unitedkingdom = "CU=ENGLAND AND CU=WALES AND CU=SCOTLAND AND CU=NORTH IRELAND"
country = "USA"
#CANADA	GERMANY	FRANCE	!ENGLAND!	JAPAN	SOUTH KOREA	PEOPLES R CHINA	INDIA	BRAZIL	SOUTH AFRICA	KAZAKHSTAN

s = 71
do = 100

dicts_from_file = []
with open('wc_list.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval('line'))

for i in range(s,do):
    driver.get('https://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?locale=en_US&errorKey=&SID=N1TMK4OsNNo7AU7gZyN&product=WOS&errorKey=&errorKey=&search_mode=AdvancedSearch&viewType=input');
    #driver.get('https://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?locale=en_US&errorKey=&viewType=input&SID=N18vVK7TxuPDKozh8s8&product=WOS&search_mode=AdvancedSearch');
    time.sleep(random.randrange(4,6))
    entertext = "DT=(article or proceedings paper or review) AND PY=2011-2015 AND WC=(" + dicts_from_file[i].rstrip() + ") AND CU=(" + country + ")"
    driver.find_element_by_id('value(input1)').send_keys(entertext)
    time.sleep(random.randrange(1,2))
    driver.find_element_by_class_name('searchButtons').click()
    time.sleep(random.randrange(1,2))
    driver.find_element_by_class_name('historyResults').click()
    time.sleep(random.randrange(1,2))
    driver.find_element_by_id('OrgEnhancedName_img').click()
    time.sleep(random.randrange(1,2))
    driver.find_element_by_name('OrgEnhancedName').click()
    time.sleep(random.randrange(1,2))
    textdata = driver.find_element_by_id('OrgEnhancedName_raMore_tr').get_attribute('innerHTML')
    file = open("WoS_WC/wc_" + dicts_from_file[i].rstrip() + "_" + str(i) + ".html","w")
    file.write(textdata)
    time.sleep(random.randrange(1,2))
    file.close()
    time.sleep(random.randrange(4,10))
print "----------------------------"
print "         all done"
print "----------------------------"
quit()
