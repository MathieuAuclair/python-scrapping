import json
import time
import requests
import urllib.request
from PIL import Image
import io

with open('file_lavitrinesag.json') as f:
    data = json.load(f)
    
    address = "https://api.pyramido.ca/v1/events?api_token=FewtJrsUnkCHfp9exx2QulBPaUbnqqmLqT69YawYqJdE1AMEFCufgtPNbDkL"
    counter = 0
    
    for activity in data:
        counter = counter + 1
        titre = activity["title"][:1] + activity["title"][1:].lower()
        
        print(activity["title"])
        print(activity["start_date"])
        print(activity["start_date"])
        print(activity["start_date"])
        print(activity["start_date"])
        print(activity["start_date"])
        print(activity["start_date"])
        
        urllib.request.urlretrieve(activity["image_url"], "beepboopboop.jpg")
        
        r = requests.post(address, data={'title': titre, 'description': activity["description"], 'date': activity["start_date"][:10]})
        print(r.status_code, r.reason)
        time.sleep(1)
        
        img = {'file': open('beepboopboop.jpg','rb')}
        
        print(json.loads(r.content)["data"]["id"])
        r2 = requests.post("https://api.pyramido.ca/v1/events/" + str(json.loads(r.content)["data"]["id"]) + "/medias?api_token=FewtJrsUnkCHfp9exx2QulBPaUbnqqmLqT69YawYqJdE1AMEFCufgtPNbDkL",  files=img)
        time.sleep(1)
