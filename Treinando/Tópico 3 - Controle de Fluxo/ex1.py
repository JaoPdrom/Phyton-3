'''
Peça ao usuário para digitar sua idade e, em seguida, 
exiba uma mensagem de acordo com a seguinte classificação:

- Se a idade for menor que 13: "Criança"
- Se a idade estiver entre 13 e 19: "Adolescente"
- Se a idade for 20 ou mais: "Adulto"

O que praticar:
Estrutura if-elif-else.
'''

idade = float(input('Informe a sua idade: '))


if idade < 13:
    print('Crianca')
elif idade >= 13 and idade <= 19:
    print('Adolescente')
else:
    print('Adulto')