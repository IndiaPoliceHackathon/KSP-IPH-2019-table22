import urllib.request
import json

number = input("Phone number.\n(with country code): +")
print(number)
data = urllib.request.urlopen("https://search5.truecaller.com/v2/search?q="+number+"&countryCode=&type=4&locAddr=&placement=SEARCHRESULTS,HISTORY,DETAILS&adId=&clientId=1&myNumber=lS59d72f4d1aefae62ba0c1979l_Dl7_DEj9CPstICL1dRnD&registerId=645710775").read()

parsed = json.loads(data)
k=json.dumps(parsed["data"], indent=4, sort_keys=True)
print(k)
#print(json.dumps(parsed["data"], indent=4, sort_keys=True)) 

for i in k.splitlines():
        print(i)
        if "firstName" in i:
            print(i)
            x=i
        if "ip" in i:
            print(i)
            y=i
        if "lastName" in i:
            print(i)
            w=i
        if "name" in i:
            print(i)
            a=i
        if "countryCode" in i:
            print(i)
            b=i
        if "dialingCode" in i:
            print(i)
            c=i
        #return x+"  "+y+"  "+w+"  "+a+"  "+b+"  "+c
        
    
        
    