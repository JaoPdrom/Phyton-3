'''
Peça ao usuário para digitar uma única letra. O 
programa deve exibir True se a letra for uma vogal (a, e, i, o, u) 
e False caso contrário. Considere apenas letras minúsculas.

O que praticar:
Operador de associação in com uma string contendo todas as vogais.
'''

letra = input('Digite uma letra: ')
letra.lower()

if 'a' or 'e' or 'i' or 'o' or 'u' in letra:
    print(True)