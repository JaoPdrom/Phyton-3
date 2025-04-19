#manipulando chaves e valores em dicionarios

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Joao Pedro'
pessoa['sobrenome'] = 'Missiagia'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

#verifica se chave existe
if pessoa.get('sobrenome') is None:
    print('Nao Existe')
else:
    print(pessoa['sobrenome'])
