#!/usr/bin/env python3

import re
import requests
import json  # Import the json module

def usernameFromUuid(uuid):
    response_text = requests.get(f'https://api.minecraftservices.com/minecraft/profile/lookup/{uuid}').text
    response_json = json.loads(response_text)
    return response_json.get("name")

if __name__ == "__main__":
    uuid = "404912f3-fa81-41e4-a135-08f80e3df0a5"
    player_uuids = ["404912f3-fa81-41e4-a135-08f80e3df0a5", "ffc9bf4f-e16e-43fb-848b-1450a2bd0390"]
    for i in player_uuids:
        print(usernameFromUuid(i))