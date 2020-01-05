import pandas as pd
import os
from os import walk
import json
# have to make two changes
#1) month wise convert json file
path = "D:/suraj/time logger/level 1/2019/sep" 
df1 = pd.read_excel("C:/Users/sanghmitra.rathore/Downloads/SURAJ DATA.xlsx")
for dirpath , dirname , filenames in walk(path):
    break

for filename in filenames:
    daydata = []
    
    df = pd.read_excel(path + "/" + filename )
    for index, row in df.iterrows():
        data = {}
        n = row[0]
        details = {}
        
        for indx, rw in df1.iterrows():
            if(rw[0] == n):
                
                data['email'] = rw[4]
               
                details['username'] = rw[0]
                break
        details['date'] = row[1]
        details['core_duration'] = row[2]
        details['total_time'] = row[3]
        data['details'] = details
        daydata.append(data)
    print(daydata)
    print("dayComplete---------------------------------------------------------")
    spl = filename.split(".")
    #make month folder manually and change the month below
    with open("D:/suraj/JsonOfLevel1/sep/" + spl[0] + ".txt", 'w') as f:
        json.dump(daydata, f, ensure_ascii=False)

