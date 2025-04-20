#set - operadores uteis
#union |
#intersection &
#difference -
#simetric difference ^

s1 = {1, 2, 3}
s2 = {2, 3, 4}
print('Set 1: ', s1)
print('Set 2: ', s2)

s3 = s1 | s2 #uniao
print('Uniao: ', s3)

s4 = s1 & s2 #interessecao
print('Intersecao: ', s4)

s5 = s1 - s2 #itens que nao estao em ambos no da esquerda
print('Diferenca: ', s5)

s6 = s2 - s1 #itens que nao estao em ambos no da esquerda
print('Diferenca: ', s6)

s7 = s1 ^ s2 #itens que nao estao em ambos
print('Diferenca simetrica: ', s7)