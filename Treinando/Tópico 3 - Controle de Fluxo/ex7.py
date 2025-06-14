'''
Peça ao usuário para criar uma senha. A senha é 
válida apenas se tiver 8 ou mais caracteres. Continue 
pedindo uma senha até que uma senha válida seja inserida. 
Quando for válida, exiba "Senha criada com sucesso!".

O que praticar:
Laço while, a função len(), if-else e break.
'''

while True:
    senha = str(input('Crie uma senha de 8 caracteres: '))
    if len(senha) < 8:
        print('Senha invalida, tente novamente')
    else:
        print('Senha criada com sucesso!')
        break