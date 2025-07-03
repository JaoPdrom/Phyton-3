'''
Crie uma função chamada imprime_info que receba um número 
indefinido de argumentos de palavra-chave (keyword arguments), 
como nome='Ana', idade=25, cidade='São Paulo'. A função deve 
imprimir cada par de chave-valor em uma nova linha.

O que praticar:
Uso de **kwargs para lidar com múltiplos argumentos nomeados.
'''

def imprime_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

imprime_info(nome='Ana', idade=25, cidade='São Paulo', profissao='Engenheira')