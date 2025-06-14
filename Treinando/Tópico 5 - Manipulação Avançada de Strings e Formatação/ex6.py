'''
Dada uma lista de palavras, como ['python', 'é', 'poderoso'], 
use o método .join() para criar uma única string onde as palavras 
são separadas por um hífen (-). A saída esperada é "python-é-poderoso".

O que praticar:
Método .join().
'''

palavras = ['python', 'é', 'poderoso']

frase_unida = '-'.join(palavras)

print('Frase unida:', frase_unida)