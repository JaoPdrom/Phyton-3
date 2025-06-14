'''
Crie uma agenda de contatos usando um dicionário onde a chave 
é o nome do contato e o valor é o seu número de telefone. O programa deve permitir ao usuário:

1. Adicionar um novo contato.
2. Consultar o telefone de um contato existente.
3. Remover um contato.
4. Listar todos os contatos.
    
Use um laço while para que o usuário possa realizar várias operações até decidir sair.
    
O que praticar:
Manipulação completa de dict (adicionar, acessar, remover com del ou .pop()), iteração com 
.items(), e controle de fluxo com while e if-elif-else.
'''

agenda = {
    'João': '123456789',
    'Maria': '987654321',
    'Pedro': '456789123'
}

while True:
    controlador = input(
        '1 - Adicionar contato\n'
        '2 - Consultar telefone\n'
        '3 - Remover contato\n' 
        '4 - Listar contatos\n'
        '5 - Sair\n'
        'Escolha uma opção: '
    )

    if controlador == '1':
        nome = input('Informe o nome do contato: ')
        telefone = input('Informe o telefone do contato: ')
        agenda[nome] = telefone
        print(f'Contato {nome} adicionado com sucesso!')

    elif controlador == '2':
        nome_busca = input('Informe o nome do contato para buscar: ')
        if nome_busca in agenda:
            print(f'Telefone de {nome_busca}: {agenda[nome_busca]}')
        else:
            print(f'Telefone de {nome_busca} nao encontrado')

    elif controlador == '3':
        nome_remover = input('Informe o nome do contato para remover: ')
        if nome_remover in agenda:
            del agenda[nome_remover]
            print(f'Contato {nome_remover} removido com sucesso!')
        else:
            print(f'Contato {nome_remover} nao encontrado')

    elif controlador == '4':
        print(agenda)

    elif controlador == '5':
        break
    
    else:
        print('Opção inválida, tente novamente.')