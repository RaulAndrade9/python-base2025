#!/usr/bin/env python3
""" Exemplos de  envio de e-mail"""

import smtplib

SERVER = 'localhost'
PORT = 8025



FROM = "test@email.com"
TO = ['destino1@server.com', 'destino2@server.com']
SUBJECT = "Meu e-mail via Python"
TEXT = """\
Ess é o meu e-mail enviado pelo Python
"""

message = f"""From: {FROM}
To: {", ".join (TO)}
Subjetc: {SUBJECT}
{TEXT}
"""

with smtplib.SMTP(host = SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode('utf-8') )