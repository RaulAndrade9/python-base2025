#!usr/bin/env python3

import logging
import os

#TODO usar função
#TODO usar lib loguru
log_level = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.Logger("logs.py",log_level )
ch = logging.StreamHandler() #console / terminal/ stderr
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s'
    'l: %(lineno)d f: %(filename)s s: %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

"""

log.debug("mensagem pro dev")
log.info("mensagem geral para usuários")
log.warning("aviso que não causa erro")
log.error("erro que afeta uma única execução")
log.critical("Erro geral ex:banco de dados sumiu")
"""

try:
    1/0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))