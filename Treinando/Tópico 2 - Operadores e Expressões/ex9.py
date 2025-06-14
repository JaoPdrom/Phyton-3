'''
Para ser aprovado em uma disciplina, o aluno precisa ter duas coisas:

1. Média final de no mínimo 7.0.
2. Frequência de no mínimo 75%.

Crie um programa que peça ao usuário sua média final (um float) e sua 
porcentagem de frequência (um int). Exiba True se o aluno foi aprovado e False caso contrário.

O que praticar:
Combinação de operadores de comparação (>=) e lógicos (and) com diferentes tipos de dados.
'''

media_final = float(input('Informe a media final: '))
porcentagem_frequencia = int(input('Informe a frequencia em porcentagem inteira: '))

if media_final >= 7 and porcentagem_frequencia >= 75:
    print(True)
else:
    print(False)