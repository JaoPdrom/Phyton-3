'''
Peça ao usuário para inserir um número. O programa deve exibir 
True se o número estiver entre 20 e 50 (inclusive) e False caso contrário.

O que praticar:

Uso do operador and para verificar duas condições simultaneamente (>= e <=).
'''

numero = float(input('Informe um numero: '))

if numero >= 20 and numero <= 50:
    print(True)
else:
    print(False)