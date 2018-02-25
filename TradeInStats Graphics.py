#Imports Modules
import csv
from itertools import zip_longest as z
from collections import Counter
from tkinter import *
from PIL import Image, ImageTk

#A - Input Path and File Details
#B - Opens File and Imports Table Creating Base Data Lists
#C - Divides Elements in Selected Types and Creates Lists for Further Processing
#D - Creates Lists for Sort and Sorts Them
#E - Creates Table for Export
#F - Set up Export File and Export
#G - Creates Graphic Display


#A - Input Path and File Details

class Window:

    def __init__(self):
        self.master = Tk()
        self.master.title('Renault Data File Information Entry')
        self.master.geometry('450x310+50+50')
        self.master.configure(bg = "#FFFFFF" )

#A1 - Miscellaneous Widgits

        self.labelEntry1 = Label(self.master, text = 'Please input the paths and names of the input and out files')
        self.labelEntry1.place(x = 10, y = 0)
        self.labelEntry1.configure(bg = '#FFFFFF')

        self.labelEntry2 = Label(self.master, text = 'The paths should have a format similar to C:/Users/Desktop/')
        self.labelEntry2.place(x = 10, y = 20)
        self.labelEntry2.configure(bg = '#FFFFFF')
        
        self.labelEntry3 = Label(self.master, text = 'Press Activate Button when done')
        self.labelEntry3.place(x = 10, y = 40)
        self.labelEntry3.configure(bg = '#FFFFFF')

        self.labelEntryIP = Label(self.master, text = 'Type in Input Path')
        self.labelEntryIP.place(x = 10, y = 65)
        self.labelEntryIP.configure(bg = '#FFFFFF')
        
        self.inputPath = StringVar()
        self.inputPathEntry = Entry(self.master, textvariable = self.inputPath)
        self.inputPathEntry.place(x = 10, y = 90)

        self.labelEntryIF = Label(self.master, text = 'Type in Input File')
        self.labelEntryIF.place(x = 10, y = 115)
        self.labelEntryIF.configure(bg = '#FFFFFF')
   
        self.inputFile = StringVar()
        self.inputPathFile = Entry(self.master, textvariable = self.inputFile)
        self.inputPathFile.place(x = 10, y = 140)

        self.labelEntryOP = Label(self.master, text = 'Type in Output Path')
        self.labelEntryOP.place(x = 10, y = 165)
        self.labelEntryOP.configure(bg = '#FFFFFF')
        
        self.outputPath = StringVar()
        self.outputPathEntry = Entry(self.master, textvariable = self.outputPath)
        self.outputPathEntry.place(x = 10, y = 190)

        self.labelEntryOF = Label(self.master, text = 'Type in Output File')
        self.labelEntryOF.place(x = 10, y = 215)
        self.labelEntryOF.configure(bg = '#FFFFFF')
   
        self.outputFile = StringVar()
        self.outputPathFile = Entry(self.master, textvariable = self.outputFile)
        self.outputPathFile.place(x = 10, y = 240)


        self.activateButton = Button(self.master, text = 'Activate', command = self.activateEntry)
        self.activateButton.place(x = 10, y = 275)
        self.activateButton.configure(fg = '#FF0000', bg = '#FFFFFF')

        self.master.mainloop()

#A2 - Commands

    def activateEntry(self):
                                     
        fileNameIP = self.inputPath.get()
        fileNameIF = self.inputFile.get()
        fileNameOP = self.outputPath.get()
        fileNameOF = self.outputFile.get()


#B - Opens File and Imports Table creating Lists

        with open(fileNameIP + fileNameIF + '.csv') as file:
            readCSV = csv.reader(file, delimiter = ',')
        
            dataList = []
            
            for row in readCSV:
             
                column2 = row[2]
                column4 = row[4]
          
                combo = [column2, column4]
        
                dataList = dataList + [combo]
        
        header  = dataList[0]
        del dataList[0]
        
        
        #C - Divides Elements in Selected Types and Creates Lists for Further Processing
        
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
        
        
        #D - Creates Lists for Sort and Sorts Them
        
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
        
        
        #E - Creates Table for Export
        
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
        
        
        #F - Set up Export File and Export
        
        preference = ['Preference', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th']
        
        newData= [preference, column1, column2, column3, column4, column5, column6, column7, column8]
        
        exportData = z(*newData, fillvalue = '')
        
        with open(fileNameOP + fileNameOF + '.csv', 'w', encoding = "ISO-8859-1", newline = '') as newFile:
              wr = csv.writer(newFile)
              wr.writerows(exportData)
              newFile.close()
              
              
#G - Creates Graphic Display

#G1 - Basic Parameters

#class WindowOut:

 #  def __init__(self):
        self.master = Tk()
        self.master.title('Trade In Preference')
        self.master.geometry('720x310+50+50')
        self.master.configure(bg = '#FFFFFF')
        
#G2 - Table Data
        self.Label0000 = Label(self.master, text = preference[0], font = 'Helvetica 8 bold', bg = "#FFFFFF")
        self.Label0000.place(x = 10, y = 0)
        self.Label0100 = Label(self.master, text = column1[0], font = 'Helvetica 8 bold', bg = "#FFFFFF")
        self.Label0100.place(x = 90, y = 0)
        self.Label0200 = Label(self.master, text = column2[0], font = 'Helvetica 8 bold', bg = "#FFFFFF")
        self.Label0200.place(x = 170, y = 0)
        self.Label0300 = Label(self.master, text = column3[0], font = 'Helvetica 8 bold', bg = "#FFFFFF")
        self.Label0300.place(x = 250, y = 0)
        self.Label0400 = Label(self.master, text = column4[0], font = 'Helvetica 8 bold', bg = "#FFFFFF")
        self.Label0400.place(x = 330, y = 0)
        self.Label0500 = Label(self.master, text = column5[0], font = 'Helvetica 8 bold', bg = "#FFFFFF")
        self.Label0500.place(x = 410, y = 0)
        self.Label0600 = Label(self.master, text = column6[0], font = 'Helvetica 8 bold', bg = "#FFFFFF")
        self.Label0600.place(x = 490, y = 0)
        self.Label0700 = Label(self.master, text = column7[0], font = 'Helvetica 8 bold', bg = "#FFFFFF")
        self.Label0700.place(x = 570, y = 0)
        self.Label0800 = Label(self.master, text = column8[0], font = 'Helvetica 8 bold', bg = "#FFFFFF")
        self.Label0800.place(x = 650, y = 0)
        
        self.Label0001 = Label(self.master, text = preference[1], bg = "#FFFFFF")
        self.Label0001.place(x = 10, y = 20)
        self.Label0101 = Label(self.master, text = column1[1], bg = "#FFFFFF")
        self.Label0101.place(x = 90, y = 20)
        self.Label0201 = Label(self.master, text = column2[1], anchor = "center", bg = "#FFFFFF")
        self.Label0201.place(x = 170, y = 20)
        self.Label0301 = Label(self.master, text = column3[1], bg = "#FFFFFF")
        self.Label0301.place(x = 250, y = 20)
        self.Label0401 = Label(self.master, text = column4[1], anchor = "center", bg = "#FFFFFF")
        self.Label0401.place(x = 330, y = 20)
        self.Label0501 = Label(self.master, text = column5[1], bg = "#FFFFFF")
        self.Label0501.place(x = 410, y = 20)
        self.Label0601 = Label(self.master, text = column6[1], anchor = "center", bg = "#FFFFFF")
        self.Label0601.place(x = 490, y = 20)
        self.Label0701 = Label(self.master, text = column7[1], bg = "#FFFFFF")
        self.Label0701.place(x = 570, y = 20)
        self.Label0801 = Label(self.master, text = column8[1], anchor = "center", bg = "#FFFFFF")
        self.Label0801.place(x = 650, y = 20)
        
        self.Label0002 = Label(self.master, text = preference[2], bg = "#FFFFFF")
        self.Label0002.place(x = 10, y = 40)
        self.Label0102 = Label(self.master, text = column1[2], bg = "#FFFFFF")
        self.Label0102.place(x = 90, y = 40)
        self.Label0202 = Label(self.master, text = column2[2], bg = "#FFFFFF")
        self.Label0202.place(x = 170, y = 40)
        self.Label0302 = Label(self.master, text = column3[2], bg = "#FFFFFF")
        self.Label0302.place(x = 250, y = 40)
        self.Label0402 = Label(self.master, text = column4[2], bg = "#FFFFFF")
        self.Label0402.place(x = 330, y = 40)
        self.Label0502 = Label(self.master, text = column5[2], bg = "#FFFFFF")
        self.Label0502.place(x = 410, y = 40)
        self.Label0602 = Label(self.master, text = column6[2], bg = "#FFFFFF")
        self.Label0602.place(x = 490, y = 40)
        self.Label0702 = Label(self.master, text = column7[2], bg = "#FFFFFF")
        self.Label0702.place(x = 570, y = 40)
        self.Label0802 = Label(self.master, text = column8[2], bg = "#FFFFFF")
        self.Label0802.place(x = 650, y = 40)
        
        self.Label0003 = Label(self.master, text = preference[3], bg = "#FFFFFF")
        self.Label0003.place(x = 10, y = 60)
        self.Label0103 = Label(self.master, text = column1[3], bg = "#FFFFFF")
        self.Label0103.place(x = 90, y = 60)
        self.Label0203 = Label(self.master, text = column2[3], bg = "#FFFFFF")
        self.Label0203.place(x = 170, y = 60)
        self.Label0303 = Label(self.master, text = column3[3], bg = "#FFFFFF")
        self.Label0303.place(x = 250, y = 60)
        self.Label0403 = Label(self.master, text = column4[3], bg = "#FFFFFF")
        self.Label0403.place(x = 330, y = 60)
        self.Label0503 = Label(self.master, text = column5[3], bg = "#FFFFFF")
        self.Label0503.place(x = 410, y = 60)
        self.Label0603 = Label(self.master, text = column6[3], bg = "#FFFFFF")
        self.Label0603.place(x = 490, y = 60)
        self.Label0703 = Label(self.master, text = column7[3], bg = "#FFFFFF")
        self.Label0703.place(x = 570, y = 60)
        self.Label0803 = Label(self.master, text = column8[3], bg = "#FFFFFF")
        self.Label0803.place(x = 650, y = 60)
        
        self.Label0004 = Label(self.master, text = preference[4], bg = "#FFFFFF")
        self.Label0004.place(x = 10, y = 80)
        self.Label0104 = Label(self.master, text = column1[4], bg = "#FFFFFF")
        self.Label0104.place(x = 90, y = 80)
        self.Label0204 = Label(self.master, text = column2[4], bg = "#FFFFFF")
        self.Label0204.place(x = 170, y = 80)
        self.Label0304 = Label(self.master, text = column3[4], bg = "#FFFFFF")
        self.Label0304.place(x = 250, y = 80)
        self.Label0404 = Label(self.master, text = column4[4], bg = "#FFFFFF")
        self.Label0404.place(x = 330, y = 80)
        self.Label0504 = Label(self.master, text = column5[4], bg = "#FFFFFF")
        self.Label0504.place(x = 410, y = 80)
        self.Label0604 = Label(self.master, text = column6[4], bg = "#FFFFFF")
        self.Label0604.place(x = 490, y = 80)
        self.Label0704 = Label(self.master, text = column7[4], bg = "#FFFFFF")
        self.Label0704.place(x = 570, y = 80)
        self.Label0804 = Label(self.master, text = column8[4], bg = "#FFFFFF")
        self.Label0804.place(x = 650, y = 80)
        
        self.Label0005 = Label(self.master, text = preference[5], bg = "#FFFFFF")
        self.Label0005.place(x = 10, y = 100)
        self.Label0105 = Label(self.master, text = column1[5], bg = "#FFFFFF")
        self.Label0105.place(x = 90, y = 100)
        self.Label0205 = Label(self.master, text = column2[5], bg = "#FFFFFF")
        self.Label0205.place(x = 170, y = 100)
        self.Label0305 = Label(self.master, text = column3[5], bg = "#FFFFFF")
        self.Label0305.place(x = 250, y = 100)
        self.Label0405 = Label(self.master, text = column4[5], bg = "#FFFFFF")
        self.Label0405.place(x = 330, y = 100)
        self.Label0505 = Label(self.master, text = column5[5], bg = "#FFFFFF")
        self.Label0505.place(x = 410, y = 100)
        self.Label0605 = Label(self.master, text = column6[5], bg = "#FFFFFF")
        self.Label0605.place(x = 490, y = 100)
        self.Label0705 = Label(self.master, text = column7[5], bg = "#FFFFFF")
        self.Label0705.place(x = 570, y = 100)
        self.Label0805 = Label(self.master, text = column8[5], bg = "#FFFFFF")
        self.Label0805.place(x = 650, y = 100)
        
        self.Label0006 = Label(self.master, text = preference[6], bg = "#FFFFFF")
        self.Label0006.place(x = 10, y = 120)
        self.Label0106 = Label(self.master, text = column1[6], bg = "#FFFFFF")
        self.Label0106.place(x = 90, y = 120)
        self.Label0206 = Label(self.master, text = column2[6], bg = "#FFFFFF")
        self.Label0206.place(x = 170, y = 120)
        self.Label0306 = Label(self.master, text = column3[6], bg = "#FFFFFF")
        self.Label0306.place(x = 250, y = 120)
        self.Label0406 = Label(self.master, text = column4[6], bg = "#FFFFFF")
        self.Label0406.place(x = 330, y = 120)
        self.Label0506 = Label(self.master, text = column5[6], bg = "#FFFFFF")
        self.Label0506.place(x = 410, y = 120)
        self.Label0606 = Label(self.master, text = column6[6], bg = "#FFFFFF")
        self.Label0606.place(x = 490, y = 120)
        self.Label0706 = Label(self.master, text = column7[6], bg = "#FFFFFF")
        self.Label0706.place(x = 570, y = 120)
        self.Label0806 = Label(self.master, text = column8[6], bg = "#FFFFFF")
        self.Label0806.place(x = 650, y = 120)
        
        self.Label0007 = Label(self.master, text = preference[7], bg = "#FFFFFF")
        self.Label0007.place(x = 10, y = 140)
        self.Label0107 = Label(self.master, text = column1[7], bg = "#FFFFFF")
        self.Label0107.place(x = 90, y = 140)
        self.Label0207 = Label(self.master, text = column2[7], bg = "#FFFFFF")
        self.Label0207.place(x = 170, y = 140)
        self.Label0307 = Label(self.master, text = column3[7], bg = "#FFFFFF")
        self.Label0307.place(x = 250, y = 140)
        self.Label0407 = Label(self.master, text = column4[7], bg = "#FFFFFF")
        self.Label0407.place(x = 330, y = 140)
        self.Label0507 = Label(self.master, text = column5[7], bg = "#FFFFFF")
        self.Label0507.place(x = 410, y = 140)
        self.Label0607 = Label(self.master, text = column6[7], bg = "#FFFFFF")
        self.Label0607.place(x = 490, y = 140)
        self.Label0707 = Label(self.master, text = column7[7], bg = "#FFFFFF")
        self.Label0707.place(x = 570, y = 140)
        self.Label0807 = Label(self.master, text = column8[7], bg = "#FFFFFF")
        self.Label0807.place(x = 650, y = 140)
        
        self.Label0008 = Label(self.master, text = preference[8], bg = "#FFFFFF")
        self.Label0008.place(x = 10, y = 160)
        self.Label0108 = Label(self.master, text = column1[8], bg = "#FFFFFF")
        self.Label0108.place(x = 90, y = 160)
        self.Label0208 = Label(self.master, text = column2[8], bg = "#FFFFFF")
        self.Label0208.place(x = 170, y = 160)
        self.Label0308 = Label(self.master, text = column3[8], bg = "#FFFFFF")
        self.Label0308.place(x = 250, y = 160)
        self.Label0408 = Label(self.master, text = column4[8], bg = "#FFFFFF")
        self.Label0408.place(x = 330, y = 160)
        self.Label0508 = Label(self.master, text = column5[8], bg = "#FFFFFF")
        self.Label0508.place(x = 410, y = 160)
        self.Label0608 = Label(self.master, text = column6[8], bg = "#FFFFFF")
        self.Label0608.place(x = 490, y = 160)
        self.Label0708 = Label(self.master, text = column7[8], bg = "#FFFFFF")
        self.Label0708.place(x = 570, y = 160)
        self.Label0808 = Label(self.master, text = column8[8], bg = "#FFFFFF")
        self.Label0808.place(x = 650, y = 160)
                  
        self.Label0009 = Label(self.master, text = preference[9], bg = "#FFFFFF")
        self.Label0009.place(x = 10, y = 180)
        self.Label0109 = Label(self.master, text = column1[9], bg = "#FFFFFF")
        self.Label0109.place(x = 90, y = 180)
        self.Label0209 = Label(self.master, text = column2[9], bg = "#FFFFFF")
        self.Label0209.place(x = 170, y = 180)
        self.Label0309 = Label(self.master, text = column3[9], bg = "#FFFFFF")
        self.Label0309.place(x = 250, y = 180)
        self.Label0409 = Label(self.master, text = column4[9], bg = "#FFFFFF")
        self.Label0409.place(x = 330, y = 180)
        self.Label0509 = Label(self.master, text = column5[9], bg = "#FFFFFF")
        self.Label0509.place(x = 410, y = 180)
        self.Label0609 = Label(self.master, text = column6[9], bg = "#FFFFFF")
        self.Label0609.place(x = 490, y = 180)
        self.Label0709 = Label(self.master, text = column7[9], bg = "#FFFFFF")
        self.Label0709.place(x = 570, y = 180)
        self.Label0809 = Label(self.master, text = column8[9], bg = "#FFFFFF")
        self.Label0809.place(x = 650, y = 180)
        
        self.Label0010 = Label(self.master, text = preference[10], bg = "#FFFFFF")
        self.Label0010.place(x = 10, y = 200)
        self.Label0110 = Label(self.master, text = column1[10], bg = "#FFFFFF")
        self.Label0110.place(x = 90, y = 200)
        self.Label0210 = Label(self.master, text = column2[10], bg = "#FFFFFF")
        self.Label0210.place(x = 170, y = 200)
        self.Label0310 = Label(self.master, text = column3[10], bg = "#FFFFFF")
        self.Label0310.place(x = 250, y = 200)
        self.Label0410 = Label(self.master, text = column4[10], bg = "#FFFFFF")
        self.Label0410.place(x = 330, y = 200)
        self.Label0510 = Label(self.master, text = column5[10], bg = "#FFFFFF")
        self.Label0510.place(x = 410, y = 200)
        self.Label0610 = Label(self.master, text = column6[10], bg = "#FFFFFF")
        self.Label0610.place(x = 490, y = 200)
        self.Label0710 = Label(self.master, text = column7[10], bg = "#FFFFFF")
        self.Label0710.place(x = 570, y = 200)
        self.Label0810 = Label(self.master, text = column8[10], bg = "#FFFFFF")
        self.Label0810.place(x = 650, y = 200)

        self.master.mainloop()
        
#G3 - Displacing the Window

Window()
    

    
