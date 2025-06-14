'''
Defina um número secreto (por exemplo, 42). Peça ao 
usuário para tentar adivinhar o número. A cada tentativa, 
diga se o palpite foi "muito alto", "muito baixo" ou se ele 
"acertou!". O jogo deve continuar até que o usuário acerte o número.

O que praticar:
Laço while, if-elif-else aninhados e o comando break.
'''

numero_secreto = 100

while True:
    numero = int(input('Digite um numero inteiro: '))

    if numero > 100:
        print('Valor digitado eh muito alto')
    elif numero < 100:
        print('Valor digitado eh muito baixo')
    else:
        print('Acertou')
        break