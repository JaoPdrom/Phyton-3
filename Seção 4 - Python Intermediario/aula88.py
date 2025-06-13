#dict comprehension e set comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritorio',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor #verifica se eh uma str
    for chave, valor in produto.items()
}

print(dc)

s1 = {i for i in range(10)}