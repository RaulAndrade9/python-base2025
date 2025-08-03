#!/usr/bin/env python3

import os
import sys

try:
    raise RuntimeError("Ocorreu um erro")
except Exception as e :
    print(f"[erro]: {str(e)}")

try: 
    input("...")#race conditions
    names = open("names.txt").readlines()
    1/0 #ZeroDivisionError
except FileNotFoundError as e: 
    print("[error]", str(e))
    sys.exit(1)
except ZeroDivisionError as r:
    print(f"[error]: {str(r)}" )
    sys.exit(1)
finally:
    print("Execute isso sempre")


print("sucesso! ")

try:
    print(names[2])
except:
    print("[error] missing name in the list")
    sys.exit(1)