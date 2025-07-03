'''
Peça ao usuário para digitar sua idade. Use o operador ternário 
para atribuir a uma variável a string "Maior de idade" se a idade 
for 18 ou mais, ou "Menor de idade" caso contrário. Exiba o resultado.

O que praticar:
Uso do operador ternário para atribuição condicional.
'''

idade = int(input("Digite sua idade: "))
print('Maior de idade' if idade >= 18 else 'Menor de idade')