'''
Crie duas listas: uma com nomes de frutas e outra com nomes de vegetais.

1. Crie uma terceira lista chamada feira que seja a combinação das duas primeiras.
2. Use o método extend para adicionar os itens da lista de vegetais à lista de frutas original. 
Exiba o resultado de ambos os casos.
    
O que praticar:
Concatenação de listas com o operador + e o método .extend().
'''

frutas = ['tomate', 'uva', 'maca', 'banana']
vegetais = ['alface', 'cenoura']

feira = frutas + vegetais
print(feira)

frutas.extend(vegetais)
print(frutas)