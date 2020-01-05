import pandas as pd
from os import walk
import os



def softTime(path): 
    DataFrame =[]
    for (dirpath,dirname,filenames) in walk (path):
        break
    print("ALl names:",filenames)   
    for filename in filenames:
        df = pd.read_excel(path+filename,index_col=None,header=[0])
        sum_core=0
        sum_ncore=0
        for index,row in df.iterrows():
            time=[]
            tym = row[2]
            time = tym.split(":")
            in_sec = int(time[0])*60*60 + int(time[1])*60 +int(time[2])
            
            if row[1]=="Core" or row[1]=="core":
                sum_core = sum_core + in_sec
            else:
                sum_ncore = sum_ncore + in_sec

        emp_name,date_xlsx =filename.split("_")
                
        date,q = date_xlsx.split(".")
                
                
        totaltime = sum_core + sum_ncore
        totalH= totaltime//3600
        totalM = (totaltime%3600)//60
        totalS = (totaltime%3600)%60
        onsystem_time = str(totalH)+":"+str(totalM)+":"+str(totalS)
        #print(sums)
        #duration = str(int((sums)//3600))+ ":"+str(int((sums-(sums//3600)*3600)//60))+":"+str(int(((sums-(sums//60)*60)*60)%60))
        h = sum_core//3600
        residual_sums = sum_core%3600
        m = residual_sums // 60
        s = residual_sums%60
        duration = str(h)+":"+str(m)+":"+str(s)
        
        #print(duration)
        
        dataf = [emp_name,date,duration,onsystem_time]
        
        DataFrame.append(dataf)
        print(filename," :Done")
    return DataFrame
print('Hello')

def starter():

    baseDir="D:/time logger/"
    #work_dir = input("Enter work location (ex. aug/30/):")
    #path = baseDir+"level 2/2019/"+ work_dir
    path="D:/time logger/program/level 1/trigger_list.xlsx"
    df=pd.read_excel(path,index_col=None,header=None)
    count=0

    for index,row in df.iterrows():
        r=row[0].split(".")
        path2=baseDir+"level 2/2020/"+r[0]+"/"+r[1]+"/"
        
        print(path2)
        DataFrame= softTime(path2)
        save_loc = baseDir+"level 1/2020/"+r[0]
        if not os.path.isdir(save_loc):
            os.makedirs(save_loc)

        save_file_name = save_loc+"/"+r[1]+".xlsx"
        writer = pd.ExcelWriter(save_file_name, engine='xlsxwriter')
        df_out=pd.DataFrame(DataFrame)
        df_out.to_excel(writer,sheet_name='sheet 1',index=None,header=["Name","Date","Core Duration","Total Time"])
        writer.save()
        
starter()
