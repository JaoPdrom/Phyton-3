"""
faça um programa que peça ao usuario para digitar um numero inteiro,
informe se esse numero eh par ou impar. Caso o usuario nao digite um numero
inteiro, informe que nao eh um numero inteiro.
"""

entrada = input('Digite um numero inteiro: ')

#solucao 1
if entrada.isdigit():
    num_int = int(entrada)%2
    if num_int == 0:
        print(f'O numero {entrada} é par')
    else:
        print(f'O numero {entrada} é ímpar')

else:
    print('Esse numero nao eh inteiro')

#solucao 2
try:
    num_int = int(entrada)%2
    if num_int == 0:
        print(f'O numero {entrada} é par')
    else:
        print(f'O numero {entrada} é ímpar')
except:
    print('Esse numero nao eh inteiro')

"""
faça um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudação apropriada a ele. Ex:
Bom dia 01-11, Boa Tarde 12-17 e Boa noite 18-23
"""
#00:00
#01234

#solucao 1
entrada = input('Informe o horario: ')

if len(entrada)!=5 or entrada[2] != ':': #verifica o formato da str
    print('Formato errado, insira no formato HH:MM')

hora = int(entrada[0]+entrada[1])
horas_minutos = int(entrada[3]+entrada[4])

if hora < 12:
    print(f'Bom dia {hora}:{horas_minutos}')
elif hora >= 12 and hora < 18:
    print(f'Boa tarde {hora}:{horas_minutos}')
elif hora >= 18:
    print(f'Boa noite {hora}:{horas_minutos}')

"""
faça um programa que peça primeiro o nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 a 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    print('Digite mais de uma letra') 
    if tamanho_nome <= 4:
        print('Seu nome é curto!')
    elif tamanho_nome >=5 and tamanho_nome <=6:
        print('Seu nome é normal!')
    else:
        print('Seu nome é muito grande!') 