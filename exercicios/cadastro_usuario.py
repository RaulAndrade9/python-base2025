#usr/bin/env python 3

#Cadastro de Usuários (dicionário + repetição)
#Crie um programa que permita cadastrar usuários com nome, email e senha em um dicionário.
#Permita também listar todos os usuários cadastrados.
#Desafio extra: verifique se o e-mail já foi cadastrado antes de inserir.

import sys
import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s %(levelname)s %(message)s",
    datefmt = "%Y - %m - %d %H:%M:%S"
)
log = logging.getLogger("cadastro_usuario.py")
usuarios = {}
while True:
    nome = input("Nome: ").strip().upper()
    if not nome:
        break
    email = input("E-mail: ")
    while email in usuarios:
        print("O e-mail já foi cadastrado. Informe outro")
        email = input("E-mail: ")
        if not email:
            break
    while not email:
        print("insira um e-mail ou tecle enter para sair")
        email = input("E-mail: ")
        if not email:
            break
    senha = input("Senha: ")
    while not senha:
        print("Informe a senha ou tecle enter para sair")
        senha = input("Senha: ")
        if not senha:
            break
    usuarios[nome] = [email, senha]
    for key, value in usuarios.items():
        print(f"Nome: {key} - e-mail: {usuarios[key][0]} - Senha: {usuarios[key][1]}")
    
    continua = input("Insira S se quiser continuar ou tecle enter para sair")
    if not continua:
        break
    

    

