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

__version__ = "0.0.1.1"
__author__ = "Carlos Vinicius"
__license__ = "Unlicense"

import os

# garantindo que pegue apenas os 4 primeiros digito da varivel de ambiente do idioma
current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US":  "Hello Word!",
    "pt_BR":  "Ola Mundo!",
    "de_DE":  "Hallo Welt!",
    "fr_FR":  "Bonjour le monde!",
    "es_SP":  "¡Hola Mundo!",
    "ru_RU":  "Привет, мир!",
    "zh_CN":  "你好，世界！",
}

# O (1) - constante - `in`
print(msg[current_language])
