"""
Iteravel -> str, range, etc 
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor
iter -> me entregue se iterador
"""

texto = iter('Joao Pedro')
iterador = iter(texto)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break

# for letra in texto:
#     print(letra)