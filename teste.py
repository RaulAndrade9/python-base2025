#!usr/bin/env python3

#Cadastro de alunos e notas
#Peça para o usuário informar o nome e três notas de cada aluno.
#Armazene tudo em um dicionário onde a chave é o nome e o valor é uma lista com as notas.
#No final, mostre a média de cada aluno e indique se ele foi aprovado (média ≥ 7) ou reprovado.

import logging


log_level = ("LOG_LEVEL", "WARNING")
log = logging.Logger("teste.py", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s'
    'l: %(lineno)d f: %(filename)s s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

notas_aluno = {}

while len(notas_aluno)<3:
    notas = []
    nome = input("informe o nome do aluno: ")
    while len(notas)<3:
        try:
            notas.append(float(input("Informe uma nota: ")))
        except ValueError as e:
            print(f"Não foi informado um valor válido para nota")
            print(f"{str(e)}")
    notas_aluno[nome] = notas

for nome, notas in notas_aluno.items():
    media_final = (sum(notas_aluno[nome]) / len(notas_aluno[nome]))
    mensagem = "Aprovado" if media_final >= 7 else "Reprovado"
    print(f"O aluno {nome} foi {mensagem}")
