import logging
import sys

ocupados = {}

try:
    for line in open("reservas.txt", encoding="utf-8"):
        nome, num_quarto, dias = line.strip().split(",")
        ocupados[int(num_quarto)] = {
            "nome": nome,
            "dias": dias
        }

except FileNotFoundError:
    logging.error("Arquivo reservas.txt não existe ")
    sys.exit()

quartos = {}

try:
    for line in open("quartos.txt", encoding="utf-8"):
        codigo,nome,preco = line.strip().split(",")
        quartos[int(codigo)] = {
            "nome": nome,
            "preco": preco, #TODO decimal
            "disponivel": False if int(codigo) in ocupados else True
        }
except FileNotFoundError:
    logging.error("Arquivo quartos.txt não existe ")
    sys.exit()

print("Reserva Hotel")
print("-" * 40)
if len(ocupados) == len(quartos):
    print("Hotel lotado")
    sys.exit(1)

nome = input("Nome do cliente: ").strip()


print("Lista de quartos disponíveis")
for codigo, dados in quartos.items():
    nome_quarto = dados["nome"]
    preco = float(dados["preco"])
    disponivel = "Not" if not dados["disponivel"] else 'Yes'
    #TODO substituir casa decimal por virgula
    print(f"{codigo} - {nome_quarto} - R${preco:.2f}")


try:
    num_quarto = int(input("Número do quarto: ").strip())
    if not quartos[num_quarto]["disponivel"]:
        print(f"O quarto {num_quarto} está ocupado")
        sys.exit(1)
except ValueError:
    logging.error("Número inválido. Entre com dígitos")
    sys.exit(1)
except KeyError:
    print(f"O quarto {num_quarto} não existe")
    sys.exit(1)

try:
    dias = int(input("Quantos dias? : ").strip())
except ValueError:
    logging.error("Informação inválida")
    sys.exit(1)

nome_quarto = quartos[num_quarto]["nome"]
preco_quarto = quartos[num_quarto]["preco"]
disponivel = quartos[num_quarto]["disponivel"]
total = float(preco_quarto * dias)

with open("reservas.txt", 'a') as file_:
    file_.write(f"{nome}, {num_quarto}, {dias}\n")

print(f"{nome} voce escolheu o quarto {nome_quarto} e vai custar{total:.2f}")