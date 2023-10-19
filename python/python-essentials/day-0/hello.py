#! /home/vinicius/miniconda3/bin/python
"""Hello World  Multi Language

Dependendo da lingua  configurada no ambiente
o programa exibe a msg corespondende.

Usage:

Tenha a variavel LANG devidamente configurada ex:
    export LANG=pt_br

Execucao:
    python3 hello.py
    or
    ./hello.py
"""

__version__ = "0.0.0.1"
__author__ = "Carlos Vinicius"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5] # garantindo que pegue apenas os 4 primeiros digito da varivel de ambiente do idioma
msg = "Hello darkness, my old friend"

if current_language == "pt_BR":
    msg = "Ola mundo :) "
# Este programa imprime Hello Word
print(msg)

