"""
Crie um sistema simples de login onde o usuário insira e-mail e senha.
Verifique os dados com base em uma lista/dicionário de usuários cadastrados.
Exiba mensagem de sucesso ou erro.
(Extra: permita cadastrar novos usuários em tempo de execução.)"""

usuarios_senhas = {
    "raul.andrade@email.com": "senha123",
    "nikelly.carvalho@email.com": "senha321",
    "buddy.cachorro@email.com": "auau123",
    "luna.gata@email.com": "miaumiau321"
}

verifica = int(input("Digite 1 para Login e 2 para Novo cadastro"))
if verifica == 1:
    login = input("Informe o login: " )
    senha = input("Informe a senha: ")
    if login in usuarios_senhas and senha == usuarios_senhas[login]:
        print("Login realizado com sucesso")
    else:
        print("Usuário ou senha inválido")
elif verifica == 2:
    login = input("Informe o usuário: ")
    senha = input("informe a senha")
    usuarios_senhas[login] = senha
    print("Usuário cadastrado com sucesso")

print(usuarios_senhas.keys())