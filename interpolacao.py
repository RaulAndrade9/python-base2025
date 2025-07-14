email_templ = """
Olá, %(nome)s,

Este produto é ótimo para resolver %(texto)s

Tem interesse em comprar este %(produto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponíveis

Preço promocional %(preco).2f
"""

clientes = ["Joao", "Maria", "Joao"]

for cliente in clientes:
    print(
        email_templ %{
            "nome": cliente,
            "produto": "caneta",
            "texto": "Escrever muito bem",
            "link": "http//canetaslegais.com",
            "quantidade": 10,
            "preco": 17.20,

        }
    )