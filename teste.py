#!usr/bin/env python3

import logging

logging.basicConfig(level=logging.WARNING,
                    format="%(asctime)s %(name)s %(message)s")
log = logging.getLogger("teste.py")

try:
    result = 1/0
    print(result)
except ZeroDivisionError as e:
    log.error(f"{str(e)}")
    