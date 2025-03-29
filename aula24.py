#operadores in e not in

nome = 'Joao'

print('a' in nome) #verifica se a letra 'a' esta no nome
print('Jo' in nome)
print(10* '-') 
print('Pe' not in nome)
print('Jo' not in nome) 

nome = input('Digite seu nome: ')
encontrar = input('Digite o quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')
