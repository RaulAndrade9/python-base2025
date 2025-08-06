"""Analisador de Texto (.txt)
Escreva um programa que leia um arquivo .txt e mostre:Quantas palavras ele possui e
Quantas vezes cada uma aparece"""

import os
path = os.curdir
filepath = os.path.join(path, "tarefa4.txt")
palavras = {}


with open(filepath, 'r', encoding='utf-8') as arquivo:
    for palavra in arquivo:
        palavra = palavra.upper()
        if palavra not in palavras:
            palavras[palavra] = 1
        else:
            palavras[palavra] +=1

for key, item in palavras.items():
    print(f"Palavra: {key} --> Quantidade: {item}")
