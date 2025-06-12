#Mapeamento de list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 30, },
    {'nome': 'p3', 'preco': 40, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} #aumenta em 0,5%
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')