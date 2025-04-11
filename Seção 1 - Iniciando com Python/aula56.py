#splits, joins

frase = '   Olha so que     , coisa legal       '
lista_frase_corrigida = frase.split(',')

#printa a que foi separada pela lista
lista_frase = []
for i, frase in enumerate(lista_frase_corrigida):
    lista_frase.append(lista_frase_corrigida[i].strip()) #remove os espacos na string no comeco e fim

print(lista_frase_corrigida)
print(lista_frase)

frases_unidas = ' - '.join(lista_frase)
print(frases_unidas)

