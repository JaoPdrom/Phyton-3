'''
Peça ao usuário para digitar seu nome completo. O programa deve verificar duas coisas:

1. Se o nome contém "Silva".
2. Se o nome NÃO começa com a letra 'Z'.

O programa deve exibir True apenas se AMBAS as condições forem verdadeiras. 
Ignore a diferença entre maiúsculas e minúsculas para a verificação de "Silva".

O que praticar: Operadores in, not, and, e métodos de string 
como .lower() e fatiamento (nome[0]).

Dica:
Converta o nome digitado para minúsculas antes de verificar a presença de "silva".
'''

nome = str(input('Insira o nome: '))
nome.lower()
if 'silva' in nome and not nome.startswith('z'):
    print(True)
else:
    print(False)