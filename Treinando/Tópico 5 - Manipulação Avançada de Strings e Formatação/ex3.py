'''
Peça ao usuário para digitar uma frase, mas com espaços 
extras no início e no fim (ex: " eu gosto de python "). 
Use um método de string para remover esses espaços e exiba a frase limpa.

O que praticar:
Método .strip().
'''

frase = input('Digite uma frase com espaços extras no início e no fim: ')

print('Frase limpa:', frase.strip())