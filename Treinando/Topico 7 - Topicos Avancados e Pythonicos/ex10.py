'''
Dada uma lista de dicionários representando produtos: 
produtos = [{'nome': 'Caneta', 'preco': 2.50}, {'nome': 'Caderno', 'preco': 15.00}, {'nome': 'Lápis', 'preco': 1.00}].

Use List Comprehension para criar uma nova lista de produtos onde:
- Se o preço for maior que R$10,00, ele deve receber um aumento de 10%.
- Caso contrário, o preço permanece o mesmo.
A nova lista deve manter a estrutura de dicionários.
    
O que praticar:
Uso de List Comprehension com uma expressão ternária no mapeamento para criar uma nova estrutura de dados complexa.
'''

produtos = [
    {'nome': 'Caneta', 'preco': 2.50}, 
    {'nome': 'Caderno', 'preco': 15.00}, 
    {'nome': 'Lápis', 'preco': 1.00}
]

lista_nova = [{**produto, 'preco': produto['preco'] * 1.10} 
              if produto['preco'] > 10 else produto 
              for produto in produtos]

print(lista_nova)