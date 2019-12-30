import pandas as pd
import openpyxl
import  xlsxwriter
from openpyxl import load_workbook , workbook
import os

#time_range is in the format (2019-11-08_2019-12-12)
#desti = "D:/suraj/time logger/level 3/2019"
desti ="C:/Users/sanghmitra.rathore/Desktop/testing/2019"
def getData( start, end , desti):
    List = [31 , 28, 31,30,31,30,31,31,30,31,30,31]
    strt = start.split("-")
    ed = end.split("-")
    if(int(strt[0])%4 == 0):
        List = [31,29,31,30,31,30,31,31,30,31,30,31]

    months = {}
    months[1] = "jan"
    months[2] = "fab"
    months[3] = "mar"
    months[4] = "apr"
    months[5] = "may"
    months[6] = "jun"
    months[7] = "july"
    months[8] = "aug"
    months[9] = "sept"
    months[10] = "oct"
    months[11] = "nov"
    months[12] = "dec"    
    if(strt[0] == ed[0]):   
        if(strt[1] == ed[1]):
            for i in range(int(strt[2]), int(ed[2])+1):
                month = months[int(ed[1])]
                if not os.path.exists(desti + "/" + month):
                    os.mkdir(desti + "/" + month)
                if(i<10):
                    day = "0" + str(i)
                else:
                    day = str(i)
                if not os.path.exists(desti + "/" + month +"/" + day):
                    os.mkdir(desti + "/" + month +"/" + day)
                print(day , month)
                word = month + "." + day
                sor = ""
                


        else:
            for i in range(int(strt[1]), int(ed[1])):
                month = months[i]
                if not os.path.exists(desti + "/" + month):
                    os.mkdir(desti + "/" + month)
                for j in range(int(strt[2]) , List[i-1]+1):
                        if(j<10):
                            day = "0" + str(j)
                        else:
                            day = str(j)
                        if not os.path.exists(desti + "/" + month +"/" + day):
                            os.mkdir(desti + "/" + month +"/" + day)
                        print(day , month)
                        word = month + "." + day
                        #prog

                strt[2] = "1"    
            for i in range(1, int(ed[2])+1):
                 month = months[int(ed[1])]
                 if not os.path.exists(desti + "/" + month):
                    os.mkdir(desti + "/" + month)
                 if(i<10):
                     day = "0" + str(i)
                 else:
                     day = str(i)
                 if not os.path.exists(desti + "/" + month +"/" + day):
                     os.mkdir(desti + "/" + month +"/" + day)
                 #prog
                 print(day ,month )
                 word = month + "." + day
        
    else:
        for i in range(int(strt[1]), 13):
            month = months[i]
            if not os.path.exists(desti + "/" + month):
                    os.mkdir(desti + "/" + month)
            for j in range(int(strt[2]), List[i-1]+1):
                if(j<10):
                    day = "0" + str(j)
                else:
                    day = str(j)
                if not os.path.exists(desti + "/" + month +"/" + day):
                    os.mkdir(desti + "/" + month +"/" + day)
                print(day,month)
                word = month + "." + day
                #pro
                

            strt[2] = "1"           
                
        for i in range(1, int(ed[1])):
            month = months[i]
            if not os.path.exists(desti + "/" + month):
                    os.mkdir(desti + "/" + month)
            for j in range(1,List[i-1]+1):
                if(j<10):
                     day = "0" + str(j)
                else:
                     day = str(j)
                if not os.path.exists(desti + "/" + month +"/" + day):
                    os.mkdir(desti + "/" + month +"/" + day)
                print(day , month)
                #prog
                word = month + "." + day

           #last month     
        for i in range(1 , int(ed[2])+1):
            month= months[int(ed[1])]
            if not os.path.exists(desti + "/" + month):
                    os.mkdir(desti + "/" + month)
            if(i<10):
                day = "0" + str(i)
            else:
                day = str(i)
            if not os.path.exists(desti + "/" + month +"/" + day):
                os.mkdir(desti + "/" + month +"/" + day)
            print( day,month )
            #prog
            word = month + "." + day
        
    
    
getData( '2019-12-19','2019-12-25' , desti )


    
    
    
    


