'''
Crie uma função chamada calcula_area que receba a largura e a 
altura de um retângulo como parâmetros e retorne sua área. Use 
argumentos nomeados ao chamar a função, invertendo a ordem 
(ex: calcula_area(altura=5, largura=10)).

O que praticar:
Chamada de função com argumentos nomeados (keyword arguments).
'''

def calcula_area(largura, altura):
    return largura * altura

print(f'A area do retangulo eh: {calcula_area(altura=5, largura=10)}')