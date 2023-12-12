#! /home/vinicius/miniconda3/bin/python

__version__ = "0.0.1.1"
__author__ = "Carlos Vinicius"
__license__ = "Unlicense"

'''
    Exibe relatorio de criancas por atividade.

    1 - Imprime a lista de criancas agrupadas por sala que frequentas cada uma
    das atividades.
'''

salas = {
    "sala_01": {
        "alunos": [
            "Carlao", "Andre", "Maicon", "Maria", "Carla", "Joao"
        ]
    },
    "sala_02": {
        "alunos": [
            "Rodolfo", "Jonas", "Eduardo", "Erik", "Douglas", "Amanda"
        ]
    }
}

aulas = {

    'ingles':{
        "alunos": [
            "Carlao", "Andre", "Jonas", "Eduardo"
        ]
    },
    'musica': {
        "alunos": [
            "Andre", "Jonas", "Erik"
        ]
    },
    'danca': {
        "alunos": [
            "Jonas", "Eduardo",  "Maria"
        ]
    },
}

for aula, info_aula in aulas.items():
    print(f"Alunos de {aula}:")
    for sala, info_sala in salas.items():
        pass


'''
for aula, info_aula in aulas.items():
    print(f"Alunos de {aula}:")
    for sala, info_sala in salas.items():
        alunos_na_sala = set(info_aula["alunos"]) & set(info_sala["alunos"])
        print(f"  - Sala {sala}: {alunos_na_sala}")
'''














