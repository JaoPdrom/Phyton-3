#List comprehension em Python
#List comprehension eh uma forma rapida de criar listas a partir de iteraveis

print(list(range(10)))

lista = []
for numero in range(10):
    if numero % 2 == 0:
        lista.append(numero)
# print(lista)

lista = [numero for numero in range(10)]
print(lista)