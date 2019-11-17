import pandas as pd
import numpy as np
data=pd.read_csv(r'finalelect3.csv')
print(data)
print(len(data))
print(data.columns)

for i in range(len(data)):
   # print(data.loc[i,"Names"])
    if data.loc[i,"Names"]=="Gopal":
        k=data.iloc[i].tolist()
        #k=k.join("  ")
        sent=k[1]+"   "+k[2]+"   "+k[3]
        print(sent)
        break;

#name=data["Names"].tolist()
#for i in len(name):
#    if(name[i]==)
    