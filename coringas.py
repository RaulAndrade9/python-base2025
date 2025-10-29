def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(item)

    print(kwargs)

#args para argumentos não nomeados e kwargs para argumentos nomeados

funcao('Raul', 35, 8500, timeout=90, sobrenome='Andrade', sexo = 'Masculino', cidade = 'SP')
