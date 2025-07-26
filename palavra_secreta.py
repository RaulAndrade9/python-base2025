#!usr/bin/env python 3

"""Jogo da forca
Jogo onde o usuário tenta acertar a palavra secreta.
Ele terá direito a até 5 tentativas.

uso:
Palavra secreta = _ _ _ _ _ _ _
tentativa = A
Palavra secreta = _ _ A _ _ A _

"""
palavra_secreta = input("Informe uma palavra: ")
tentativas = 5
lista = ["_"] * len(palavra_secreta)
lista_erradas = []
tentativa_palavra = ""

print(lista)
while tentativas >=0:
    letra = input("Informe uma letra ")
    if letra in palavra_secreta:
        print("Parabéns, voce acertou uma letra")
        for i in range(0, len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                lista[i] = letra
        print(lista)
    else:
        print("Essa letra não está na palavra secreta")
        lista_erradas.append(letra)
    tentativa_palavra = input("Qual a palavra?")
    if tentativa_palavra == palavra_secreta:
        print(f"Parabéns! Voce acertou a palavra: {palavra_secreta}")
        break
    tentativas -= 1