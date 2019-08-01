# -*- coding: utf-8 -*-
import time
import random
import textwrap
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
from selenium.common.exceptions import NoSuchElementException


entertext1 = """(pubyear < 2016 and Pubyear > 2010 and (DOCTYPE (ar) or DOCTYPE (cp) or DOCTYPE (re)) and AFFILCOUNTRY ( ( russian  federation  AND china) or ( russian  federation  AND India) or ( russian  federation  AND Brazil) or ( russian  federation  AND south africa)  or ( China  AND India) or (china AND Brazil) or ( China  AND South Africa)  or ( India  AND Brazil) or ( India  AND South Africa) or ( Brazil  AND South Africa))"""
#print textwrap.wrap(entertext1, 2)
#with open ('texttest.txt', 'w') as inf:
f1 = open('./texttest.txt', 'w')
#entertext1 = textwrap.wrap(entertext1, 2)
e1 = list(map(''.join, zip(*[iter(entertext1)]*110)))
f1.write(str(e1))

#print len(str(entertext1))
print str(e1)
