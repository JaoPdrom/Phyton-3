#documentacao https://docs.python.org/3/library/stdtypes.html
#tipos imutaveis: str, int, float, bool

string = 'joao Pedro'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(outra_variavel)
print(string)
print(string.capitalize()) #primeira letra maiuscula
print(string.zfill(100)) #preenche a str com 0 a esquerda 