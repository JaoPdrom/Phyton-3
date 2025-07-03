'''
Dada a lista de dicionários use a função sorted() junto com 
uma função lambda para ordenar a lista de alunos pela nota, em ordem decrescente.
alunos = [{'nome': 'Ana', 'nota': 9}, {'nome': 'Bruno', 'nota': 7}, {'nome': 'Carla', 'nota': 8}], 

O que praticar:
Uso de lambda como a key para a função sorted().
'''

alunos = [
    {'nome': 'Ana', 'nota': 9}, 
    {'nome': 'Bruno', 'nota': 7}, 
    {'nome': 'Carla', 'nota': 8}
]

ordena = sorted(alunos, key=lambda x: x['nota'], reverse=True)
print(ordena)

#key= define o criterio de ordenação
#lambda x: dict inteiro 
#x['nota'] valor da chave nota do dict
#reversed=True para ordenar em ordem decrescente