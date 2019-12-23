import pandas as pd
import os
from os import walk
from os import walk
import xlrd
import xlsxwriter




app = "Photoshop"
fpath = "D:/suraj/time logger/level 2/2019/dec"
month = "Dec"
def app_list(app, fpath , month):
   
    orignal = []
    semi = []
   
    for (dirpath, dirname, filenames) in walk(fpath):
        break
    for dirr in dirname :
        #print(dirr)
        namelist = []
        date = dirr
        duration = []
        for (dirpath, dirname, filenames) in walk(fpath + "/" + dirr):
            break
        
        for filename in filenames:
            df = pd.read_excel(fpath + "/" + dirr + "/" +filename, index_col=None , header = [0])
            
            for index, row in df.iterrows():
                if(row[0] == app):
                   filen = filename.split("_")
                   name = filen[0]
                   
                   namelist.append(name)
                   duration.append(row[2])
                else:
                    continue
        td=0
        for tm in duration :
            spl = tm.split(":")
            splh = int(spl[0])*60*60
            splm = int(spl[1])*60
            spls = int(spl[2])
            total = splh+splm+spls
            td=td + total
        
        time=td
        
        orignal.append([date, namelist , td])

    print(orignal)               
                    
                
         


    writer = pd.ExcelWriter(month+'.xlsx', engine='xlsxwriter')
    df_out=pd.DataFrame(orignal)
    df_out.to_excel(writer,sheet_name='sheet 1',index=None,header=["Date" , "User", "Duration"])
    writer.save()        
            
           
   
    


app_list(app , fpath)
