import pandas as pd
import xlsxwriter
import shutil
from os import walk
import os
import xlsxwriter
from app_list import app_list

from contextlib import redirect_stdout
applistpath = "D:/suraj/time logger/program/permission list"
path ="D:/suraj/time logger/level 2"
path2 ="C:/Users/sanghmitra.rathore/Desktop/testing"


def allAppList(path,path2, applistpath):
    for(dirpath, dirname, filenames) in walk(path):
        break
    npath=""
    for dirr in dirname:
        if not os.path.exists(path2 + "/" + dirr):
            os.mkdir(path2 + "/" + dirr)
            npath=path2 + "/" + dirr
                    
        for(dirpath, dirname, filenames) in walk(path + "/" +dirr):
            break
       
        for months in dirname:
            if not os.path.exists(path2 + "/" + dirr + "/" + months):
                os.mkdir(path2 + "/" + dirr + "/" + months)
            df = pd.read_excel(applistpath + "/" + "core_app_list.xlsx" , index_col = None , header=[0])
            fpath = path + "/" +dirr + "/" + months 
            destination = path2 + "/" + dirr + "/" + months
            for index , row in df.iterrows():
                app =row[0]
                print("in side app", app)
                app_list(app, fpath, months , destination)   
            print("Done")
        break       

        
allAppList(path, path2, applistpath)




