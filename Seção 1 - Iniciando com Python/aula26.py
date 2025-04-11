#formatacao basica de strings
#s - string
#d - int
#f - float

var = 'abc'
print(f'{var}')

#padding - posicionamento da string
print(f'{var:1>10}') #preenche 10 caracteres a esquerda com numeros 1
print(f'{var:2<10}') #preenche 10 caracteres a direita com numeros 2
print(f'{var:0^10}') #centraliza a string com numeros 0
print(10*'-')
print(f'{1000.8945775843:.1f}') #arredonda para 1 casa decimal
print(f'{1000.8945775843:,.1f}') #arredonda para 1 casa decimal e separa por virgula
print(f'{1000.8945775843:0>+10.1f}') #arredonda para 1 casa decimal e preenche os espacos com 0