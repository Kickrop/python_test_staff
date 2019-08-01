# -*- coding: utf-8 -*-
import xlwings as xw
wb1 = xw.Book() #create a new file
wb = xw.Book('test1.xlsx') #connect to an existing filename
#wb = xw.Book(r'C:/path/to/file.xlsx')

xw.apps[0].books['test1.xlsx']

sht = wb.sheets['Sheet1']
sht1 = wb1.sheets[0]
#xw.Range('A1').value #active sheet
#wb.sheets[0].range('A1').value #first sheet
#sht.range('A1').value = 'Foo 1' #write
#showme = sht.range('A1').value  #read
#showme = sht.range('A1').expand().value

showme = sht.range('A1:D10').value
showme2 = sht.range('D1:D10').value
showme1 = sht['A1:D7']

for i in range(1,8):
    sht1.range('A' + str(i)).value = showme[i-1] #return content of excel sheet
    #sht1.range('B' + str(i)).value = showme[i-1]
    #print showme[i]

#sht1.range('B1').value = showme2[0]
#print showme[0], showme2[0], showme1[0]
