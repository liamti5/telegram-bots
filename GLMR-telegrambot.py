# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 09:53:55 2022

@author: liamt
"""

import requests
from datetime import datetime

def getInfo():
    parameters = {
        "row": 1,
        "page": 1,
        "address": "0xdB4Ff740721A1d2ebD4B040CD0c4a7d794DEA141"
    }
    
    response = requests.get("https://moonbeam.api.subscan.io/api/scan/account/reward_slash", 
                            params = parameters)
    
    eventID = response.json()["data"]["list"][0]["event_index"]
    reward = float(response.json()["data"]["list"][0]["amount"])/10**18
    time = datetime.fromtimestamp(response.json()["data"]["list"][0]["block_timestamp"])
    
    return time, f"EventID {eventID}: {reward} GLMR"

text = getInfo()

urls = "https://api.telegram.org/bot5132716808:AAHdavWm0kFveXmrqudv8CinhONvqJ3HtOY/sendMessage"

response = requests.post(url = urls, data = {"chat_id": 1372941487, "text": f"{text}"}).json()

print(response)

