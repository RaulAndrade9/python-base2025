import logging
import sys
log = logging.Logger("alerta")

info = {
    "temperatura": None,
    "umidade": None
}

keys = info.keys()
for key in keys:
    try:
        info[key] = float(input(f"Informe a {key} " ).strip())
    except ValueError :
        log.error(f"{key.capitalize()} inválida")
        sys.exit(1)


temperatura = info["temperatura"]
umidade = info["umidade"]

if temperatura > 45:
    print("Frio extremo")
elif temperatura * 3 >= umidade:
    print("Calor úmido")
elif temperatura >= 10 and temperatura <=30:
    print("temperatura normal")
elif temperatura >=0 and temperatura <10:
    print("Frio")
else:
    print("Frio extremo")