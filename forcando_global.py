nome = 'Global'

def funcao():
    nome = 'Local'
    nome = globals()['nome']
    print('Nome Local: ', nome)


funcao()