import urllib.request
import json

number = input("Phone number.\n(with country code): +")

data = urllib.request.urlopen("https://search5.truecaller.com/v2/search?q="+number+"&countryCode=&type=4&locAddr=&placement=SEARCHRESULTS,HISTORY,DETAILS&adId=&clientId=1&myNumber=lS59d72f4d1aefae62ba0c1979l_Dl7_DEj9CPstICL1dRnD&registerId=645710775").read()

parsed = json.loads(data)

print(json.dumps(parsed["data"], indent=4, sort_keys=True)) 