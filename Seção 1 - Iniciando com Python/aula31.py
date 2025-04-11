#flag - marca lugar
#none - nao valor
#is e is not 
#id

#id
v1 = 'a'
v2 = 'b'
print(id(v1))
print(id(v2))

#flags
condicao = True
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Nao faca algo')


if passou_no_if is None:
    print('Nao passou no if')
else:
    print('Passou no if')