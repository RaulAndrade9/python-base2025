contador = 0


def funcao():
    global contador
    contador += 1
    subcontador = 0

    def funcao_interna():
        global contador
        contador +=1
        nonlocal subcontador
        subcontador += 1
        return subcontador

    funcao_interna()
    



funcao()
funcao()
print(contador)

