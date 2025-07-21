#!usr/bin/env python3
"""Hello world multi linguas.
Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente

Como usar: 
Tenha a variável LANG devidamente configurada
ex:
    export LANG=pt_BR

Ou informe através do CLI argument "--lang"

Ou o usuário terá que digitar

Execução:
    python3 hello.py
"""
__version__ = "0.1.3" #dunder
__author__ = "Raul Andrade"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    #TODO: tratar value error
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid option {key}")
        sys.exit()
    arguments[key] = value


current_language = arguments["lang"]
if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language")

current_language = current_language[:5]

msg = {
    "pt_BR": "Olá, Mundo !",
    "it_IT": "Ciao, Mondo !",
    "es_SP": "Hola, Mundo !",
    "fr_FR": "Bonjour, Monde !",
    "en_US": "Hello, World"
}



print(msg[current_language] *int(arguments["count"]))
