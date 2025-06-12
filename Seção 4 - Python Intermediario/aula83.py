#empacomaneto e desempacotamento de dicts
a, b = 1, 2
a, b = b, a
print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# a, b = pessoa #keys
# print(f'Keys: {a, b}')
# a, b = pessoa.values() #valores das keys
# print(f'Values: {a, b}')
# a, b = pessoa.items() #keys e valores
# print(f'Itens: {a, b}')

dados_pessoa = {
    'idade': 16,
    "altura": 1.6,
}

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)

#kwargs
def mostra_args_nomeados(*args, **kwargs):
    print(kwargs)

# mostra_args_nomeados(nome='Joana', qlq=123)
mostra_args_nomeados(**pessoa_completa)