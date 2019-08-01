# -*- coding: utf-8 -*-

import time
import random
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
from selenium.common.exceptions import NoSuchElementException

#unitedkingdom = "CU=ENGLAND AND CU=WALES AND CU=SCOTLAND AND CU=NORTH IRELAND"
#country = "UK(all)"
country = "GERMANY"
#USA CANADA	GERMANY	FRANCE	!ENGLAND!	JAPAN	SOUTH KOREA	PEOPLES R CHINA	INDIA	BRAZIL	SOUTH AFRICA	KAZAKHSTAN

s = 0
do = 251 #251

dicts_from_file = []
with open('wc_list.txt','r') as inf:
    for line in inf:
        dicts_from_file.append(eval('line'))
#print "\nbegins\n" + str(datetime.datetime.now())
for i in range(s,do):
    driver.get('https://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?SID=P2TLWgeFquwhOz2PgzO&product=WOS&replaceSetId=&goToPageLoc=SearchHistoryTableBanner&search_mode=AdvancedSearch&errorQid=1#SearchHistoryTableBanner');
    time.sleep(random.randrange(1,2))
    driver.find_element_by_id('value(input1)').clear()
    #driver.get('https://apps.webofknowledge.com/WOS_AdvancedSearch_input.do?locale=en_US&errorKey=&viewType=input&SID=N18vVK7TxuPDKozh8s8&product=WOS&search_mode=AdvancedSearch');
    time.sleep(random.randrange(1,2))
    entertext = "DT=(article or proceedings paper or review) AND PY=2011-2015 AND WC=(" + dicts_from_file[i].rstrip() + ") AND CU=(" + country + ")"
    #entertext = "DT=(article or proceedings paper or review) AND PY=2011-2015 AND WC=(" + dicts_from_file[i].rstrip() + ") AND (CU=ENGLAND OR CU=WALES OR CU=SCOTLAND OR CU=NORTH IRELAND)"
    time.sleep(random.randrange(1,2))
    driver.find_element_by_id('value(input1)').send_keys(entertext)
    time.sleep(random.randrange(2,3))
    driver.find_element_by_class_name('searchButtons').click()
    time.sleep(random.randrange(2,3))
    try:
        driver.find_element_by_class_name('historyResults').click()
        time.sleep(random.randrange(3,4))
        driver.find_element_by_id('OrgEnhancedName_img').click()
        time.sleep(random.randrange(1,2))
        driver.find_element_by_name('OrgEnhancedName').click()
        time.sleep(random.randrange(1,2))
        textdata = driver.find_element_by_id('OrgEnhancedName_raMore_tr').get_attribute('innerHTML')
        file = open("WoS_WC/" + country + "_wc_" + dicts_from_file[i].rstrip() + "_" + str(i) + ".html","w")
        file.write(textdata)
        time.sleep(random.randrange(1,2))
        file.close()
        time.sleep(random.randrange(2,3))
    except NoSuchElementException:
        print dicts_from_file[i].rstrip() + " not found"
        time.sleep(random.randrange(1,2))
        file = open("WoS_WC/errors_" + country + "_wc_" + dicts_from_file[i].rstrip() + "_" + str(i) + ".txt","w")
        time.sleep(random.randrange(1))
        file.write(entertext)
        driver.find_element_by_id('value(input1)').clear()
        time.sleep(random.randrange(1,2))
    #if i == 199:
        #driver.find_element_by_name('bselsets').click()
        #time.sleep(random.randrange(1,2))
        #driver.find_element_by_name("src='https://images.webofknowledge.com/WOKRS522_2R1/images/delsets.gif'")
print "----------------------------"
print "         all done " + str(do)
print "----------------------------"
quit()
