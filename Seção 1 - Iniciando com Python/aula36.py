#operadores de atribuição
# = =+ *= /= //= **= %=

contador = 0
while contador <= 10:
    if contador % 2 == 0:
        print(f'O numero {contador} eh par')
    else:
        print(f'O numero {contador} eh impar')
    contador += 1
print('Saiu')
