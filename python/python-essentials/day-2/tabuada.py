#! /home/vinicius/miniconda3/bin/python

__version__ = "0.0.1.1"
__author__ = "Carlos Vinicius"
__license__ = "Unlicense"

# imprima a tabuada do 1 ao 10

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range(1, 11))

for numero in numeros:
    print("{:-^18}".format(f"Tabuada do: {numero}"))

    print()

    for outro_numero in numeros:
        resultado = numero * outro_numero
        print("{:^18}".format(f"{numero} x {outro_numero} = {resultado} "))
        print()
    print("#" * 18 )
    print()

