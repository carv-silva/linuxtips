#! /home/vinicius/miniconda3/bin/python
"""Cadastro de produto"""

__version__ = "0.0.1.0"
__author__ = "Carlos Vinicius"
__license__ = "Unlicense"

import pprint


produto = {
    "nome": "Canetas",
    "cores": ["azul", "branco"],
    "preco": 3.23,
    "dimensao": {
        "altura": 12.1,
        "largura": 0.8,
    },
    "produto_em_estoque": True,
    "codigo": "45678",
    "cod_de_barra": None,
}

cliente = {
    "nome": "Carlos"
}

# quantidade = None

compra = {
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}

# pprint.pprint(compra)
total_compra = compra["quantidade"] * compra["produto"]["preco"]
pprint.pprint(
    f"O cliente {compra['cliente']['nome']}"
    f" comprou {compra['quantidade']} unidades de {compra['produto']['nome']}"
    f" e pagou o total de {total_compra}"
)

