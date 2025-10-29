#começa o escopo global
nome = "global"
numero = 1
flag  = True

def funcao():
    #aqui começa o escopo local
    def funcao_interna():#inner function / closure
        #aqui começa o escopo local da função interna
        nome = 'interna' 
        return nome

    return "Olá"
    #aqui termina o escopo local



#aqui termina o escopo global