#Mapeamento de list comprehension - filter

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 30, },
    {'nome': 'p3', 'preco': 40, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} #aumenta em 0,5%
    if produto['preco'] > 20 else {**produto} #mapeamento
    for produto in produtos
    if produto['preco'] > 10 # filtro
]

# print(novos_produtos)
print(*novos_produtos, sep='\n')

lista2 = [n for n in range(10) if n < 5]
# print(lista2)

'''
RESUMINDO

lista = [(mapeamento) for ... (filter)]

'''