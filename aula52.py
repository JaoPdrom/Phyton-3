#tupla - uma lista imutavel

#maneiras de definir uma tupla com ou sem parenteses
nome =  'Maria', 'Luiz', 'Pedro'
nome =  ('Maria', 'Luiz', 'Pedro')
print('Tuplas nome: ', nome, type(nome))

#conversao de uma lista para uma tupla
lista = ['Maria', 'Luiz', 'Pedro']
print('Lista: ', lista, type(lista))
lista = tuple(lista)
print('Lista convertida em tupla: ', lista, type(lista))

#conversao de tupla em lista
lista = list(lista)
print('Tupla convertida em tupla: ', lista, type(lista))