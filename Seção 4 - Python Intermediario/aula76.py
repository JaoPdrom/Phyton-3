pessoa = {
    'nome': 'joao Pedro',
    'Sobrenome': 'Missiagia',
    'idade': 20,
    'altura': 1.8,
    'enderecos': [
        {'rua': 'rua de rau', 'numero': 123},
        {'rua': 'outra rua de rau', 'numero': 321},
    ],
}

print(pessoa, type(pessoa))
print(pessoa['nome'])

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')