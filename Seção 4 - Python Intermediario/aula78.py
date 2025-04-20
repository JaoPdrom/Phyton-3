#sets - conjuntos em python
#tipo mutavel que aceita tipos imutaveis
#eficiente para remover valores duplicados
#nao garantem ordem
#nao aceitam valores mutaveis
#nao tem indexes
#sao iteraveis

# s1 = set()
# s1 = {'Luiz', 1, 2, 3}

s1 = {1, 2, 3, 3, 3, 3, 1}
print(s1)
print(1 in s1)
print(5 in s1)

for valor in s1:
    print(valor)