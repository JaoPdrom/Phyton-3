'''
Peça ao usuário para inserir a largura e a altura de um retângulo. 
Calcule a área (largura * altura) e o perímetro (2 * (largura + altura)) e exiba os resultados.

O que praticar:
Operadores aritméticos * e +, uso de parênteses para precedência.
'''

altura = float(input('Informe a altura: '))
largura = float(input('Informe a largura: '))

area = largura * largura
perimetro = (2 * (largura+largura))

print(f'O perimetro eh {perimetro}')
print(f'O area eh {area}')