'''
Crie uma tupla com as coordenadas (x, y), por exemplo, (10, 20). 
Tente alterar o primeiro valor da tupla para 15. Observe o erro 
(TypeError) e explique em um comentário no código por que ele acontece.

O que praticar:
Entendimento da imutabilidade de tuple.
'''

tupla = (10, 20)
print(tupla)

tupla[0] = 15

#o erro ocorre pois tuplas sao tipos de dados imutaveis
#portanto nao podem ser alterados, para modificar sera necessario
#uma nova tupla