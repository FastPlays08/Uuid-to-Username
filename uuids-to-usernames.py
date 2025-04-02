#!/usr/bin/env python3
from converter import *
import time  # Import the time module


mode = input("Mode?\n1. uuid:username\n2. username\nDefault=1\n")

try:
    if mode == "":
        mode = 1
    mode = int(mode)
except ValueError:
    print("Not an option")
    exit()

start_time = time.time()

with open('uuids.txt', "r") as uuids, open('output.txt', 'w') as out_file:
    if mode == 2:
        for line in uuids:
            if line.endswith(".dat\n"):
                uuid = line[:-5]
            else:
                print("Line is not a .dat file, passing")
                continue
            out_file.write(usernameFromUuid(uuid) + "\n")
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

print(f"Execution time: {time.time() - start_time:.2f} seconds")