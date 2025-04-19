"""
higher order functions
funcoes de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)


v = executa(saudacao, 'Bom dia', 'Joao')
print(v)