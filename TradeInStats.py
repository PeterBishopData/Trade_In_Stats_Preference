#Imports Modules
import csv
from itertools import zip_longest as z
from collections import Counter

#A - Opens File and Imports Table Creating Base Data Lists
#B - Divides Elements in Selected Types and Creates Lists for Further Processing
#C - Creates Lists for Sort and Sorts Them
#D - Creates Table for Export
#E - Set up Export File and Export


#A - Opens File and Imports Table creating Lists

with open('Input.csv') as file:
    readCSV = csv.reader(file, delimiter = ',')

    dataList = []
    
    for row in readCSV:
     
        column2 = row[2]
        column4 = row[4]
  
        combo = [column2, column4]

        dataList = dataList + [combo]

header  = dataList[0]
del dataList[0]


#B - Divides Elements in Selected Types and Creates Lists for Further Processing

#Counts Elements in Model Types

elementType = []
elementCount = []

dataList.sort()

previous = '#'

for row in dataList:

    if row == previous:
        previous = row
    else:
        elementType = elementType + [row]
        elementCount = elementCount + [dataList.count(row)] # from collections

        previous = row
     

#Creates Data Count Lists

counter = 0
 
captur = []
capturCount = []
 
clio = []
clioCount = []
 
fluence = []
fluenceCount = []

megane = []
meganeCount = []

for row in elementType:

    make = row[0]
    tradeIn = row[1]
    
    value = elementCount[counter]
    
    if make == 'Captur':
        captur = captur + [tradeIn]
        capturCount = capturCount + [value]
        
    elif make == 'Clio':
        clio = clio + [tradeIn]
        clioCount = clioCount + [value]

    elif make == 'Fluence':
        fluence = fluence + [tradeIn]
        fluenceCount = fluenceCount + [value]

    elif make == 'Megane':
        megane = megane + [tradeIn]
        meganeCount = meganeCount + [value]
        
    counter = counter + 1


#C - Creates Lists for Sort and Sorts Them

#Captur
capturSort = []
intermediate = []

counter = 0
alpha = 0
beta = 0

for row in captur:

    alpha = row
    beta = capturCount[counter]

    intermediate = [alpha, beta]
        
    capturSort = capturSort + [intermediate]

    counter = counter + 1

capturSort.sort(key = lambda x: x[1], reverse = True)

#Clio
clioSort = []
intermediate = []

counter = 0
alpha = 0
beta = 0

for row in clio:

    if counter < 10:
        alpha = row
        beta = clioCount[counter]

        intermediate = [alpha, beta]

        clioSort = clioSort + [intermediate]

        counter = counter + 1

clioSort.sort(key = lambda x: x[1], reverse = True)

#Fluence
fluenceSort = []
intermediate = []

counter = 0
alpha = 0
beta = 0

for row in fluence:

    alpha = row
    beta = fluenceCount[counter]

    intermediate = [alpha, beta]

    fluenceSort = fluenceSort + [intermediate]

    counter = counter + 1

fluenceSort.sort(key = lambda x: x[1], reverse = True)


#Megane
meganeSort = []
intermediate = []

counter = 0
alpha = 0
beta = 0

for row in megane:

    alpha = row
    beta = meganeCount[counter]

    intermediate = [alpha, beta]

    meganeSort = meganeSort + [intermediate]

    counter = counter + 1

meganeSort.sort(key = lambda x: x[1], reverse = True)


#D - Creates Table for Export

#Creates Table to prevent Data Shift

column1 = ['Captur']
column2 = ['Count']
column3 = ['Clio']
column4 = ['Count']
column5 = ['Fluence']
column6 = ['Count']
column7 = ['Megane']
column8 = ['Count']

counter = 1

for counter in range (1, 30):

    column1 = column1 + [' ']
    column2 = column2 + [' ']
    column3 = column3 + [' ']
    column4 = column4 + [' ']
    column5 = column5 + [' ']
    column6 = column6 + [' ']
    column7 = column7 + [' ']
    column8 = column8 + [' ']
    
    counter = counter + 1


#Set up Captur Data for Export

counter = 1

cellCount = len(capturSort)

for cell in capturSort:

    if counter <= cellCount:
        column1[counter] = cell[0]
        column2[counter] = cell[1]

    counter = counter + 1


#Set up Clio Data for Export

counter = 1

cellCount = len(clioSort)

for cell in clioSort:

    if counter <= cellCount:
        column3[counter] = cell[0]
        column4[counter] = cell[1]

    counter = counter + 1
    

#Set up Fluence Data for Export

counter = 1

cellCount = len(fluenceSort)

for cell in fluenceSort:

    if counter <= cellCount:
        column5[counter] = cell[0]
        column6[counter] = cell[1]

    counter = counter + 1  


#Set up Megane Data for Export

counter = 1

cellCount = len(meganeSort)

for cell in meganeSort:

    if counter <= cellCount:
        column7[counter] = cell[0]
        column8[counter] = cell[1]

    counter = counter + 1  


#E - Set up Export File and Export

preference = ['Preference', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']

newData= [preference, column1, column2, column3, column4, column5, column6, column7, column8]

exportData = z(*newData, fillvalue = '')

with open('C:/Users/Peter/Documents/Peter - Toshiba/Python Project/Renault Trade Ins/Output.csv', 'w', encoding = "ISO-8859-1", newline = '') as newFile:
      wr = csv.writer(newFile)
      wr.writerows(exportData)
      newFile.close()
    
print('All Done')
    
