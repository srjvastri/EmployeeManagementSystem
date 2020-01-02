import pandas as pd
from os import walk
bigdata = []
v=[]
name_list=[]
lvl2_applist=[]
mid ={}
#mdata = {'email':'','name':'','data':{'2019-12-30':[['core','total'],['illustratore','core','duration']]}}
mdata = {'email':'','name':'','data':{'2019-12-30':[['core','total'],['illustratore','core','duration']]}}
v.append('0')

path="D:\\time logger\\applist\\user.xlsx"
df = pd.read_excel(path,index_col=None,header=[0])

for index,row in df.head(5).iterrows():
    mdata = {'email':'','name':'','data':''}
    mdata['email']=row[1]
    mdata['name']= row[0]
    name_list.append(row[0])    
    bigdata.append(mdata)
    

print(bigdata)

month = ['dec','nov','oct']
days = {}
days['dec'] = 31
days['nov'] = 30
days['oct'] = 31

path_lv1 = "D:\\time logger\\level 1\\2019\\dec\\"
#path_lv1 = "D:\\time logger\\level 1\\2019\\" + month[0] + "\\"

path_lv2 = "D:\\time logger\\level 2\\2019\\dec\\01\\"
#path_lv2 = "D:\\time logger\\level 1\\2019\\" + month[0] + "\\" str(days[month[0]]) + "\\"


for (dirpath,dirname,filenames) in walk (path_lv1):
        break

day_list =filenames
#print(filenames)

for (dirpath,dirname,filenames) in walk (path_lv2):
        break
    
filenames_lvl2 = filenames
#print(filenames_lvl2)
user_name=[]

for f in filenames_lvl2:
    #print(f)
    n = f.split("_")
    user_name.append(n[0])
  

#print(user_name)


for name in name_list:
    df = pd.read_excel(path_lv1+"01.xlsx",header=[0],index_col=None)
    
    for index,row in df.iterrows():
        
        #print(row[0],name)
        #print(name)
        if name == row[0]:
            print(name)
            lvl2_applist.append([row[2],row[3]])
            df_lv2 = pd.read_excel(path_lv2+name+"_01122019.xlsx",header=[0],index_col=None)
            
            for i,r in df_lv2.iterrows():
                ls=[]
                ls.append(r[0])
                ls.append(r[1])
                ls.append(r[2])
                lvl2_applist.append(ls)
            #print(lvl2_applist)
        
            #mdata['data']["2019-12-01"]=lvl2_applist

    for i in bigdata:
        if i['name']==name:
            mid[row[1]]=lvl2_applist
            i['data']=mid
    lvl2_applist=[]
    mid={}
print(bigdata)
                

    
