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

__version__ = "0.0.1.0"
__author__ = "Carlos Vinicius"
__license__ = "Unlicense"

import os

# garantindo que pegue apenas os 4 primeiros digito da varivel de ambiente do idioma
current_language = os.getenv("LANG", "en_US")[:5]
msg = "Hello darkness, my old friend"

# aqui temos uma ordem de complexidade O(n) <- estudar este topico dps
if current_language == "pt_BR":
    msg = "Ola mundo :) "
elif current_language == "de_DE":
    msg = "Hallo Welt!"
elif current_language == "fr_FR":
    msg = "Bonjour le monde!"
elif current_language == "es_ES":
    msg = "¡Hola Mundo!"
elif current_language == "ru_RU":
    msg = "Привет, мир!"
elif current_language == "zh_CN":
    msg = "你好，世界！"


print(msg)
