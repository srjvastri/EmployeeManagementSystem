import pandas as pd
from os import walk
import os
import xlrd
from openpyxl import load_workbook

epath = "D:/suraj/SURAJ DATA.xlsx"
path = "D:/suraj/time logger/level 2/2019/dec"

for dirpath , dirname , filenames in walk(path):
    break

for dirr in dirname:
    pa= path + "/" + dirr
    for dirpth , dirnme , filenmes in walk(pa):
        break
    for file in filenmes:
        name = file.split("_")
        #print(file)
        readFile = pd.read_excel(path + "/" +dirr + "/" + file)
        df = pd.read_excel(epath)
        #print("hello")
        for index , row in df.iterrows():
            if(row[0].lower() == name[0].lower()):
                print("found")
                for indx , rw in readFile.iterrows():
                    
                    rw['d'] = "its here"
                    break
                print(readFile)    
                
