<<<<<<< HEAD
input('Qual o seu nome? ')
=======
#aula de input

#input registra em str

nome = input('Qual o seu nome? ') #registra em nome o input
print(nome) #mostra o dado de nome
print(f'seu nome eh:{nome=}') #mostra a variavel e o valor nela

numero_1 = input('Digite um numero: ')
numero_2 = input('Digite um outro numero: ')
print(f'A soma dos numeros eh: {numero_1 + numero_2}') #str concatenada

#correcao eh fazer typecast
numero_1 = int(input('Digite um numero: '))
numero_2 = int(input('Digite um outro numero: '))
print(f'A soma dos numeros eh: {numero_1 + numero_2}')
#probelema: caso nao seja digitado um int, uma str por exemplo, da erro
>>>>>>> 430fa00 (first commit)
