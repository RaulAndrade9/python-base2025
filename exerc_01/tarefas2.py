"""Fça um programa que solicite ao usuário o nome de um livro e a nota por
linha de comando, uma breve resenha(através do input) e depois grave em um arquivo
da seguinte maneira
Livro:
Nota:
Resenha:
"""

import sys
import os
path = os.curdir
filepath = os.path.join(path, "tarefa2.txt")
arguments = sys.argv[1:]
*nome, nota = arguments
if len(nome)>1:
    nome = " ".join(nome)
else:
    nome = nome[0]
resenha = input("Descreva uma breve resenha do livro\n")

with open(filepath, "a", encoding='utf-8')as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Nota: {nota}\n")
    arquivo.write(f"Resenha \n{resenha}")