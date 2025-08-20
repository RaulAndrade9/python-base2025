#!usr/bin/env python 3
"""Faça um programa que imprima números pares de 1 a 200
"""
for i in range(1,201):
    if i % 2 != 0:
        continue
    else: print(i,end=", ")