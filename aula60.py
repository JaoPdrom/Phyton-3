#operacoes terminarias
# <valor> if <condicao> else <outro valor>

# condicao = True
# variavel = 'Valor' if condicao else 'Outro Valor'
# print(variavel)

digito = 1
novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito >= 9 else digito
print(novo_digito)