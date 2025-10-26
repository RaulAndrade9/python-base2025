#!usr/bin/env python 3
#Gerenciador de Tarefas (lista de dicionários)
#O programa deve permitir:
#adicionar uma tarefa (titulo, descricao, status),
#marcar tarefa como concluída,
#listar todas as tarefas.
#Salve e carregue as tarefas de um arquivo .txt.


import logging
import sys
import os

logging.basicConfig(
    level=logging.DEBUG,
    format= "%(asctime)s %(levelname)s %(message)s"
)
log = logging.getLogger("tarefas.py")

path = os.curdir
filepath = os.join.path(path,"tarefas.txt")

lista  = []
titulo = "Lista de Tarefas"
print(titulo.center(50, "-"))

#add tarefa
titulo_tarefa = input("Título da tarefa: ")
descricao = input("Descrição da tarefa: ")
status = input("Status da tarefa: ")
with open (filepath, 'a', encoding="utf-8") as arquivo:
    arquivo.write(titulo_tarefa, descricao, status, "\n")