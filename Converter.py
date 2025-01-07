#!/usr/bin/env python3

from UuidToName import *

with open('uuids.txt') as fp:
    for line in fp:
        uuid = line[:-5]
        print(uuid)
        print(usernameFromUuid(uuid))
