'''
Crie um dicionário para um contato, com nome e telefone. 
Peça ao usuário para adicionar um novo campo, como email, 
e seu respectivo valor. Em seguida, atualize o número de 
telefone do contato para um novo valor e exiba o dicionário final.

O que praticar:
Adição de novos pares chave-valor e atualização de valores existentes em um dict.
'''

pessoa = {
    'nome': 'Joao Pedro',
    'telefone': '123456789'
}

campo = input('Informe um novo campo: ')
valor_campo = input('Informe um valor para o campo: ')
pessoa[campo] = valor_campo

pessoa['telefone'] = input('Informe o novo telefone: ')
print(pessoa)