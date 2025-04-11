# operadores logicos - and
# sera verdadeiro apenas se todas as condicoes forem True

entra = input('[E]entrar [S]air: ')
senha_digitada = input('Digite a senha: ')

senha_permitida = '123456'

if entra == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(True and True and True)
print(True and True and False)