'''
Crie uma lista de dicionários, onde cada dicionário representa 
um aluno e contém as chaves nome e notas (uma lista de 3 notas). Exemplo:

alunos = [
    {'nome': 'Alice', 'notas': [8, 9, 7]},
    {'nome': 'Bob', 'notas': [6, 7, 5]},
    {'nome': 'Carlos', 'notas': [10, 9, 9.5]}
]

Escreva um programa que itere sobre essa lista e calcule a média de 
cada aluno. Ao final, exiba o nome do aluno e sua respectiva média.

O que praticar:
Iteração sobre uma lista de dicionários, acesso a valores aninhados 
(uma lista dentro de um dicionário), e cálculo com os dados obtidos.
'''

alunos = [
    {'nome': 'Alice', 'notas': [8, 9, 7]},
    {'nome': 'Bob', 'notas': [6, 7, 5]},
    {'nome': 'Carlos', 'notas': [10, 9, 9.5]}
]

for aluno in alunos:
    media = 0
    #armazena nota do aluno e as soma
    for nota in aluno['notas']:
        media += nota

    #conta a quantidade de notas do aluno
    contador = 0
    for nota in aluno['notas']:
        contador += 1

    #calcula a media
    media /= contador
    print(f'Media {aluno['nome']} eh {media:.2f}')


#versao utilizando a funcao sum e len
# for aluno in alunos:
#     media = sum(aluno['notas']) / len(aluno['notas'])
#     print(f'Media {aluno['nome']} eh {media:.2f}')