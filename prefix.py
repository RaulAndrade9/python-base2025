#!/usr/bin/env python 3
"""Calculadora prefix.
Funcionamento:

[operação] [n1] [n2]

operações:
sum -> +
sub -> 
mul -> *
div -> /

uso: 
$prefix.py sum 5 2
7

$prefix.py mul 10 5
50

$prefix.py
operacao: sum
n1: 5
n2: 4
9

"""
__version__ = "0.1.0"

import sys

arguments = sys.argv[1:]

if not arguments:
    operacao = input("Informe a operação: ")
    n1 = int(input("Informe o n1: "))
    n2 = int(input("informe o n2: "))
else:
    operacao, n1,n2 = arguments
    n1 = int(n1)
    n2 = int(n2)

if operacao == "sum":
    result = n1 + n2
elif operacao == "sub":
    result= n1-n2
elif operacao == "mul":
    result = n1*n2
else:
    result = n1/n2

print(f"Operação: {operacao}")
print(f"n1: {n1}")
print(f"n2: {n2}")
print(result)