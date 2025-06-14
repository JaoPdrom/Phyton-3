'''
Para entrar em um evento, a pessoa precisa ser maior de idade 
(18 anos ou mais) OU estar acompanhada por um responsável. 
Crie um programa que pergunte a idade do usuário e se ele está 
com um responsável (peça para digitar 'sim' ou 'não'). Exiba True 
se o acesso for permitido e False caso contrário.

O que praticar:

Combinação dos operadores lógicos or e and com operadores de comparação >= e ==.
'''

idade = int(input('Informa a sua idade: '))

if idade < 18:
    acompanhante = input('Menor de idade, esta acompanhado de uma adulto? [SIM/NAO]: ') 
    if acompanhante.lower() == 'nao':
        print(False)
    else:
        print(True)
else:
    print(True)