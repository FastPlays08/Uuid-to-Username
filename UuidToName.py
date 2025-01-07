#!/usr/bin/env python3

import re
import requests

def getInfo(uuid):
    response = requests.get(f'https://playerdb.co/api/player/minecraft/{uuid}')
    text_response = response.text
    return text_response

def findUserNameInResponse(response):
    x=response[135:153]
    match = re.search('"([^"]*)"', x)
    if match:
        return match.group(0)
    else:
        return f"Could not find username for uuid: '{uuid}'"

def usernameFromUuid(uuid):
    return findUserNameInResponse(getInfo(uuid))

#print("Initial response: "+text_response)
#print("Matching in: "+x)

if __name__ == "__main__":
    uuid="404912f3-fa81-41e4-a135-08f80e3df0a5"
    print(usernameFromUuid(uuid))
