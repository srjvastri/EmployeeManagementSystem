import pandas as pd
from os import walk
import os

#path = "D:/temp_report/bej/"
#DataFrame = []
#for (dirpath,dirname,filenames) in walk ("D:/temp_report/bej"):
 #    break

#print(filenames)
#for filename in filenames :
#    df = pd.read_excel(path+filename, index_col=None , header=[0])
#    name = "Bejoy"
#    app =  "CINEMA 4D"
#    #print(filename)
#    s = filename.split("_")
#    u=s[1].split(".")
    #print(u[0])
    
#    for index, row in df.iterrows():
#         if(row[0] == "CINEMA 4D" ):
#             row['d'] = u[0]
             #print(row)
             
             
 #            DataFrame.append(row)
             
            
             #print(row)
  

#writer = pd.ExcelWriter(name+'.xlsx', engine='xlsxwriter')
#df_out=pd.DataFrame(DataFrame)
#df_out.to_excel(writer,sheet_name='sheet 1',index=None,header=["Appname","C/N","Core Duration", "dates"])
#writer.save()

        
path = "D:/temp_report/vig/"
DataFrame = []
for (dirpath,dirname,filenames) in walk ("D:/temp_report/vig"):
     break

#print(filenames)
for filename in filenames :
    df = pd.read_excel(path+filename, index_col=None , header=[0])
    name = "vignesh"
    app =  "CINEMA 4D"
    #print(filename)
    s = filename.split("_")
    u=s[1].split(".")
    #print(u[0])
    ls=[]
    a = u[0][0]+u[0][1]+'-'+u[0][2]+u[0][3]+'-'+u[0][4]+u[0][5]+u[0][6]+u[0][7]
    
    for index, row in df.iterrows():
         if(row[0] == "CINEMA 4D" ):
             row['d'] = a
             
             #print(row)
             
             
             DataFrame.append(row)
             
            
             #print(row)
  

writer = pd.ExcelWriter(name+'.xlsx', engine='xlsxwriter')
df_out=pd.DataFrame(DataFrame)
df_out.to_excel(writer,sheet_name='sheet 1',index=None,header=["Appname","C/N","Core Duration", "dates"])
writer.save()

