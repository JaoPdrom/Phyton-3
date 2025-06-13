#for dentro de for list comprehension

lista = []
for x in range(10):
    for y in range(10):
        lista.append((x, y))

lista = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(lista)