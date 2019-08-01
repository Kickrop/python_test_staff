# -*- coding: utf-8 -*-
import xlwings as xw
import os, sys
wb1 = xw.Book() #create a new file
#wb = xw.Book('test1.xlsx') #connect to an existing filename
#wb = xw.Book(r'C:/path/to/file.xlsx')

#xw.apps[0].books['test1.xlsx']

#sht = wb.sheets['Sheet1']
path = "H:/python/xls"
os.chdir(path)
inputfiles = os.listdir(path) #os.getcwd()
nfdir = len(inputfiles)
for j in range(0,nfdir):    #nfdir
    #excel_file = file = open(inputfiles[j],"r")
    wb = xw.Book(j)

    sht = wb.sheets[1]

    sht1 = wb1.sheets[0]




#xw.Range('A1').value #active sheet
#wb.sheets[0].range('A1').value #first sheet
#sht.range('A1').value = 'Foo 1' #write
#showme = sht.range('A1').value  #read
#showme = sht.range('A1').expand().value

    showme = sht.range('A11:U394').value
    showme2 = sht.range('D1:D10').value
    showme1 = sht['A1:D7']

    for i in range(1,395):
        sht1.range('A' + str(i)).value = str(sht)
        sht1.range('B' + str(i)).value = showme[i-1] #return content of excel sheet
    #print showme[i]
#print sht
#sht1.range('B1').value = showme2[0]
#print showme[0], showme2[0], showme1[0]
