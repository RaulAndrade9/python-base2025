#!/usr/bin/env python3

"""Exemplos de funções"""

def heron(a,b,c):
    perimeter = a + b + c
    s = perimeter / 2
    area = s * (s - a) * (s-b) * (s-c)
    return area ** 0.5

def heron2(params):
    #a, b, c = params
    return heron(*params)

triangulos = [
    (3,4,5),
    (5,12,13),
    (5,2,8),
    (13,22,10),
    (89,84,97)
]

for t in triangulos:
    area = heron2(t)
    print(f"A área do triângulo é: {area}")

print(list(map(heron2, triangulos)))