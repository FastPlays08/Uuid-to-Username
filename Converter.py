#!/usr/bin/env python3
from UuidToName import *

mode = input("Mode?\n1. uuid:username\n2. username\nDefault=1\n")

try:
    mode = int(mode)
except ValueError:
    pass

with open('uuids.txt') as uuids, open('output.txt','a') as out_file:
    if mode == 2:
        for line in uuids:
            if line.endswith(".dat\n"):
                uuid = line[:-5]
            else:
                print("Line is not a .dat file, passing")
                continue
            out_file.write(usernameFromUuid(uuid)+"\n")
        print("Done!")
    else:
        for line in uuids:
            if line.endswith(".dat\n"):
                uuid = line[:-5]
            else:
                print("Line is not a .dat file, passing")
                continue
            username = usernameFromUuid(uuid)
            out_file.write(f'{uuid}:{username}\n')
        print("Done!")
