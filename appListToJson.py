import pandas as pd
from os import *
import xlsxwriter



mainfile = "C:/Users/sanghmitra.rathore/Desktop/testing3/2019_done/dec/Illustrator.xlsx"
path = "C:/Users/sanghmitra.rathore/Desktop/testing3/2019_done"
def toJson(mainfile , path):
    print("function called")
    df = pd.read_excel(mainfile)
    for dirpath , dirname , filenames in walk(path):
        break
    #here dirr month except current month
    print("wtf")
    for dirr in dirname:
        currMonths=mainfile.split("/")
        allMonths = len(currMonths)
        if(dirr == currMonths[allMonths -2]):
            continue
        else:
            for dirpth , dirnme , filenmes in walk(path + "/" + dirr):
                break
            for file in filenmes:
                if(currMonths[allMonths -1] == file):
                    print(str(dirr))
                    dff = pd.read_excel(path + "/" +str(dirr) + "/" + file)
                
                
                    df = df.append(dff  )
                
                



    writer = pd.ExcelWriter(path + "/appList.json" , engine = 'xlsxwriter')
    df_out = pd.DataFrame(df)
    df_out.to_excel(writer , sheet_name = 'Sheet 1' , index=None, header = None)
    writer.save()
    



toJson(mainfile , path)
