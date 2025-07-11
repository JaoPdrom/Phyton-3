'''
Crie dois dicionários: 
perfil = {'nome': 'João', 'idade': 25} e 
contato = {'email': 'joao@example.com', 'telefone': '1234-5678'}. 
Use o operador de desempacotamento de dicionários (**) para criar 
um terceiro dicionário chamado perfil_completo que contenha todas 
as chaves e valores dos dois dicionários originais.

O que praticar:
Desempacotamento de dicionários (**) para mesclagem.
'''

perfil = {'nome': 'João', 'idade': 25}
contato = {'email': 'joao@example.com', 'telefone': '1234-5678'}

perfil_completo = {**perfil, **contato}

for chave, valor in perfil_completo.items():
    print(f"{chave}: {valor}")