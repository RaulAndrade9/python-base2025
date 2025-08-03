#!/usr/bin/env python3

import os
import sys

if os.path.exists("names.txt"):
    input("...")#race conditions
    names = open("names.txt").readlines()
else: 
    print("[error] file names.txt not found")
    sys.exit(2)

if len(names) >= 3:
    print(names[2])
else:
    print("[error] missing name in the list")
    sys.exit(1)