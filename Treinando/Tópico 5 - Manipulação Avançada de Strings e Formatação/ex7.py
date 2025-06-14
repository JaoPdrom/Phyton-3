'''
Peça ao usuário para digitar o nome de uma organização 
ou conceito (ex: "Organização das Nações Unidas"). Crie 
um programa que gere o acrônimo correspondente (ex: "ONU").

O que praticar:

Combinação de .split(), iteração sobre a lista resultante e 
fatiamento para pegar a primeira letra de cada palavra.
'''
# input('Digite o nome de uma organização ou conceito: ')
nome = 'Organização das Nações Unidas'
palavra = nome.split()

acronimo = []

for indice in range(len(palavra)):
    if palavra[indice][0] == palavra[indice][0].upper():
        acronimo.append(palavra[indice][0])

print(''.join(acronimo))