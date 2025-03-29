#formatacao de string

nome = 'Joao'
altura = 1.76
peso = 89.0
imc = peso / (altura*altura)

#f-string
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc eh:'
linha_3 = f'{imc:.2f}'
print(linha_1)
print(linha_2, linha_3)