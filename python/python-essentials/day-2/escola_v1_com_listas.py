#! /home/vinicius/miniconda3/bin/python

__version__ = "0.0.1.0"
__author__ = "Carlos Vinicius"
__license__ = "Unlicense"

'''
    Exibe relatorio de criancas por atividade.

    1 - Imprime a lista de criancas agrupadas por sala que frequentas cada uma
    das atividades.
'''


sala1 = ["Carlao", "Andre", "Maicon", "Maria", "Carla", "Joao"]
sala2 = ["Rodolfo", "Jonas", "Eduardo", "Erik", "Douglas", "Amanda"]

aula_ingles = ["Carlao", "Andre", "Jonas", "Eduardo" ]
aula_musica = ["Andre", "Jonas", "Erik"]
aula_danca = ["Jonas", "Eduardo",  "Maria"]

atividades = [
    ("Ingles", aula_ingles),
    ("Musica", aula_musica),
    ("Dança", aula_danca),
]
atividade_sala1 = []
atividade_sala2 = []


for nome_atividade, atividade in atividades:
    print(f"Alunos da atividade: {nome_atividade} \n")
    # print("-*-" * 35)
    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        if aluno in sala2:
            atividade_sala2.append(aluno)
        # if aluno in aula_danca:
            # nada ainda
    print(f"Sala 01: {atividade_sala1}")
    print(f"Sala 02: {atividade_sala2} \n")
    print("-*-" * 28)


