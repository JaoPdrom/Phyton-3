'''
Peça ao usuário para digitar um CPF no formato XXX.XXX.XXX-XX. Verifique se a string digitada:

1. Contém 14 caracteres.
2. Tem pontos (.) nas posições corretas (índices 3 e 7).
3. Tem um hífen (-) na posição correta (índice 11).
Exiba "Formato válido" ou "Formato inválido".  

O que praticar:
Função len(), fatiamento preciso e operadores lógicos.
'''

cpf = input('Digite seu CPF no formato XXX.XXX.XXX-XX: ')

if len(cpf) == 14 and cpf[3] == '.' and cpf[7] == '.' and cpf[11] == '-':
    print('Formato válido')
else:
    print('Formato inválido')