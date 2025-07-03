'''
Crie um programa que pergunte o nome de um produto, 
seu preço (float) e a quantidade comprada (int). Em 
seguida, formate e exiba uma linha de um recibo, alinhando 
os valores. O nome do produto deve ser alinhado à esquerda em 
20 caracteres, a quantidade centralizada em 10 caracteres, e o 
preço total (preço * quantidade) alinhado à direita com 2 casas 
decimais em 15 caracteres.

Exemplo de saída:
Produto               Quantidade      Preço Total
--------------------------------------------------
Mouse sem fio             10           R$    750.00
Teclado Mecânico           5           R$   1250.50
'''

produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
quantidade = int(input("Digite a quantidade comprada: "))

preco_total = preco * quantidade

print(f"{'Produto':<20}{'Quantidade':^10}{'Preço Total':>15}")
print("-" * 50)
print(f'{produto:<20}{quantidade:^10}{preco_total:>15.2f}')