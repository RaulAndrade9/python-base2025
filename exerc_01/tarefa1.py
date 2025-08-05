"""Tarefa:
Leia um arquivo .txt contendo nomes (um por linha).
Crie outro arquivo que contenha apenas os nomes em letras maiúsculas, ordenados em ordem alfabética."""

import os
path = os.curdir
filepath = os.path.join(path, "tarefa1.txt")
nomes = []
with open(filepath, 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        nomes.append(linha.upper().strip('\n'))

print(sorted(nomes))