#!/usr/bin/env python3

import requests
import json

def usernameFromUuid(uuid: str):
    response_text = requests.get(f'https://api.minecraftservices.com/minecraft/profile/lookup/{uuid}').text
    response_json = json.loads(response_text)
    return response_json.get("name")

def uuidFromUsername(username: str):
    response_text = requests.get(f"https://api.minecraftservices.com/minecraft/profile/lookup/name/{username}").text
    response_json = json.loads(response_text)
    return response_json.get("id")

if __name__ == "__main__":
    name = "fastplays08"
    print(uuidFromUsername(name))
    player_uuids = ["404912f3-fa81-41e4-a135-08f80e3df0a5", "ffc9bf4fe16e43fb848b1450a2bd0390"]
    for i in player_uuids:
        print(usernameFromUuid(i))

    