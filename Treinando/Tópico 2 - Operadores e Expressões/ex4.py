'''
Defina um nome de usuário e uma senha em variáveis. 
Peça ao usuário para digitar um nome de usuário e uma senha. 
Exiba True se AMBOS, o nome de usuário e a senha, estiverem corretos, e False caso contrário.

**O que praticar:**

Operadores de igualdade == e o operador lógico and.
'''

nome_usario = 'testepython'
senha = '1234Jpen@'

nome_usuario_inserido = str(input('Informe o nome de usuario: '))
senha_inserida = str(input('Informa a senha: '))

if nome_usuario_inserido == nome_usario and senha_inserida == senha:
    print(True)
else:
    print(False)