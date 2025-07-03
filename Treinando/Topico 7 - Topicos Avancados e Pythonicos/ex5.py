'''
Dada a string "python", crie um dicionário onde cada chave é 
uma letra da string e o valor é o número de vezes que a letra 
aparece. Use Dict Comprehension e o método .count().

O que praticar: Sintaxe de Dict Comprehension.

Saída esperada:
{'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1} (se a palavra fosse "banana", seria {'b': 1, 'a': 3, 'n': 2}).
'''


palavra = input("Digite uma palavra: ").lower()

dicionario = {letra: palavra.count(letra) for letra in set(palavra)}
# letra: sera a chave
# palavra.count(letra): sera o valor .count(letra) conta o numero de ocorrencias da letra dentro da string

print(dicionario)

for letra, quantidade in dicionario.items():
    print(f'{letra}: {quantidade}')