#definição ou atribuição
#assinatura + typehints
#documentação  docstring
#codigo
#valor de retorno

#-parametros
#posicional - passados em ordem

def nome_da_funcao(a:int, b:int, c:int) -> int:
    """descrever o que a função faz

    use esta função quando quiser a+b+c
    quando o parametro a tiver o valor 10, vai acontecer X

    :param a: numero inteiro
    :type a: int
    :param b: numero inteiro
    :type b: int
    :param c: numero inteiro
    type c: int
    :return: retorna o resultado da soma de a,b e c
    rtype: int

    >>> nome_da_funcao(1,2,3)
    6

    """

    resultado = a+b+c
    return resultado

#função com muitos argumentos
valor = nome_da_funcao(
    a=1,
    b=2,
    c=3,
    
)

#passagem de argumentos nomeados
nome_da_funcao(a=1, b=3, c=5)
print(nome_da_funcao(1,2,3))

#######################################

def outra_funcao(a,b,c):
    """explica o que faz a função
    """
    #tupla como valor de retorno
    return a * 2, b * 2, c * 2

valor1, valor2, valor3 = outra_funcao(1,2,3)
#pegar apenas o valor1
valor1, *_ = outra_funcao(1,2,3)
print(valor1, valor2, valor3)

#########################################

#passagem de argumentos com desempacotamento

def soma(n1, n2):
    """faz a soma de dois números"""
    return n1 +n2

#argumentos em sequência
args = (10,20)
print(soma(*args))#desempacota os argumentos de maneira posicional

#argumentos dicionário 
args = {"n2": 90, "n1": 100}
print(soma(**args))# 2*(**) servem para desempacotar elementos que possuem dois valores por posição(dict, hashmap)

lista_de_valores_somar = [
    {"n2": 90, "n1": 100},
    {"n2": 90, "n1": 300},
    {"n2": 90, "n1": 85}
]

for item in lista_de_valores_somar:
    print(soma(**item))