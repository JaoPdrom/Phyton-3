#operador logico or
# considera toda expressao verdadeira se uma condicao for verdadeira

entra = input('[E]entrar [S]air: ')
senha_digitada = input('Digite a senha: ')

senha_permitida = '123456'

if (entra == 'E' or entra =='e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')

print(False or False or 0 or 'abc')
print(True or True or False)
