#exercicio com while
#iterando strings com while
#       0123456789
nome = 'Joao Pedro'
tamanho_nome = len(nome)
nova_string = ''
controle = 0

while controle < tamanho_nome:
    letra = nome[controle]
    nova_string += f'*{letra}'
    controle += 1
nova_string += '*'
print(nova_string)