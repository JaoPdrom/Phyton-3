#metodos uteis em sets

s1 = set()
s1.add('luiz') #adiciona um valor por vevz
s1.add(1) #adiciona um valor por vez

s1.update('Ola mundo')
print(s1)

s1.update(('Ola mundo', 1, 2, 3, 4)) #passa um iteravel
print(s1)

s1.discard('Ola mundo') #elimina um valor
print(s1)

s1.clear()
print(s1)
