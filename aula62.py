"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = '39319307857'
nove_digitos = cpf[:9] #coleta os 9 primeiro digitos do cpf

contador_1 = 10
resultado_valor_1 = 0

for valor_1 in nove_digitos:
    resultado_valor_1 += int(valor_1) * contador_1 #multiplica e soma os valores
    contador_1 -= 1

dig_1 = (resultado_valor_1 * 10) % 11 #obtem o modulo
dig_1 if dig_1 <= 9 else 0 #verifica se o dig1 eh menor ou igual 9



dez_digito = nove_digitos + str(dig_1) #recebe os nove_digitos + o dig1 convertido para str
contador_2 = 11
resultado_valor_2 = 0

for valor_2 in dez_digito:
    resultado_valor_2 += int(valor_2) * contador_2 #multiplica e soma os valores
    contador_2 -= 1 
dig_2 = (resultado_valor_2 * 10) % 11
dig_2 if dig_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{dig_1}{dig_2}' #monta a str cpf_gerado
print(cpf_gerado)

if cpf_gerado == cpf:
    print('O CPF eh valido')
else:
    print('CPF invalido')