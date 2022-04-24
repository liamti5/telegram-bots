# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 12:19:01 2022

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
    
    return print(time, f"EventID {eventID}: \n{reward} GLMR")

getInfo()
