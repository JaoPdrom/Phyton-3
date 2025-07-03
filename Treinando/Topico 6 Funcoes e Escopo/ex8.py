'''
Crie uma variável global contador = 0. Crie uma função chamada 
incrementa que tente aumentar o valor do contador em 1.

1. Primeiro, tente fazer isso sem a palavra-chave global. Chame 
a função e veja se o contador global mudou.
2. Depois, altere a função para usar a palavra-chave global 
e veja a diferença no resultado.

O que praticar:
Entendimento do escopo de variáveis e o uso da palavra-chave 
global para modificar variáveis de escopo externo.
'''

contador = 0

def incrementa():
    global contador
    #necessario ter o global para acessar a variavel que esta fora do escopo da função
    #se nao tiver o global, o python entende que é uma variavel local
    contador += 1

incrementa()
print(f"Valor do contador após a chamada da função: {contador}")