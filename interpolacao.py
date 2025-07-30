#!/usr/bin/env python3
import os
import sys

arguments = sys.argv[1:]
filename = arguments[0]
templatename = arguments[1]
if not arguments:
    print("Informe o nome do arquivo de e-mails")
    sys.exit(1)

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


for line in open(filepath):
    name, email = line.split(",")
    
    print(f"Enviando e-mail para {email}")
    print()
    print(
        open(templatepath).read() %{
            "nome": name,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "http//canetaslegais.com",
            "quantidade": 10,
            "preco": 17.20,


        }
    )
    print("-" * 50)