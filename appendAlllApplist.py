import pandas as pd
from os import walk
import xlsxwriter
import json


filepath = "C:/Users/sanghmitra.rathore/Desktop/testing/2019_done/dec"
def func(filepath):
    List = []
    for dirpath , dirnames , filenames in walk(filepath):
        break
    for file in filenames:
        print(file)
        df = pd.read_excel(filepath + "/" + file)
        for index , row in df.iterrows():
            dirr = {}
            dirr["Date"] = row[0]
            dirr["All Users"] = row[1]
            dirr["Total Duration"] = row[2]

            List.append(dirr)
    print(List)
    
    with open('data.json', 'w') as f:
        json.dump(List , f)



func(filepath)
