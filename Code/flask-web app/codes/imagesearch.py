# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 05:58:42 2019

@author: SAMARTH G VASIST
"""

import requests, json

url = "http://localhost:5000/search"

data = {
    "image_url":"http://placehold.it/350x150.png",
    "resized_images":False, # Or True
    "cloud_api":True
}


headers = {'Content-type': 'application/json'}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r)
#r.json to get the response as json
#print(r.json())
