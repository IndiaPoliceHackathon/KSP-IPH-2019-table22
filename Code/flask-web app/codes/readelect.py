import pandas as pd
p=open("electordetails.txt","r")
f=p.readlines()
names=[]
Hno=[]
Sex=[]

for i in f:
    print(i)
    k=i.split(' | ')
    if(len(k)>6):
        print(k)
        names.append(k[3].strip())
        print(k[2])
        Hno.append(k[2].strip())
        #m=k[6].split(':')[1]
        print(k[6])
        Sex.append(k[6].strip())
    print(k)
print(len(names))
print(len(Sex))
print(len(Hno))    
print(names)
print(Sex)
print(Hno)
df = pd.DataFrame(list(zip(names,Sex,Hno)),columns =['Names', 'Sex','HouseNumber']) 
print(df)
df.to_csv('finalelect3.csv') 