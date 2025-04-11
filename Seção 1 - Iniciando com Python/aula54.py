"""
Faça uma lista de compas com listas.
O usuario deve ter a possibilidade de inserir, apagar e listar valores
da sua lista. Não permita que o programa quebre com erros de 
indices inexistentes na lista
"""
import os

lista_compras = []

#solucao 1
while True:
    entrada = input('[I]nserir novo item na lista, [L]istar itens, [D]eletar itens, [S]air: ').lower()
    
    #saida do programa
    if(entrada == 's'):
        break

    #insere na lista
    if(entrada == 'i'):
        os.system('cls')
        item_a_ser_inserido = input('Informe o item a ser inserido: ')
        lista_compras.append(item_a_ser_inserido)

    #mostra itens na lista
    elif(entrada == 'l'):
        os.system('cls')
        if len(lista_compras) == 0: #verifica se a lista eh vazia
            print('Lista vazia!')
        
        for i, item in enumerate(lista_compras): #exibe a lista com os indices
            print(i+1, item)

    #deleta item da lista com base no nome
    elif(entrada == 'd'):
        os.system('cls')
        if not lista_compras: #verifica se a lista esta vazia antes de deletar
            print('Lista vazia!')

        for i, item in enumerate(lista_compras): #exibe a lista com os indices
            print(i+1, item)

        try:
            item_a_ser_deletado = int(input('Informe o indice do item a ser deletado: ')) - 1
            del lista_compras[item_a_ser_deletado]

            for i, item in enumerate(lista_compras): #exibe a lista com os indices
                print(i+1, item)
        except ValueError: #tratamento de erro de valor imcopativel inserido
            print('Digite um numeo inteiro')
        except IndexError: #tratamento de erro de valor imcopativel inserido
            print('Erro! Indice nao existe')

    else:
        print('Valor invalido! Informe o valor correto. ')


#solucao 2
while True:
    entrada = input('[I]nserir novo item na lista, [L]istar itens, [D]eletar itens, [S]air: ').lower()
    
    #saida do programa
    if(entrada == 's'):
        break

    #insere na lista
    if(entrada == 'i'):
        item_a_ser_inserido = input('Informe o item a ser inserido: ')
        lista_compras.append(item_a_ser_inserido)

    #mostra itens na lista
    elif(entrada == 'l'):
        if not lista_compras: #verifica se a lista eh vazia
            print('Lista vazia!')
        print(lista_compras) #mostra a lista

    #deleta item da lista com base no indice
    elif(entrada == 'd'):
        if not lista_compras: #verifica se a lista esta vazia antes de deletar
            print('Lista vazia!')

        for indice, item in enumerate(lista_compras, 1): #enumera a lista começando o 1
            print(f'{indice}, {item}')

        item_a_ser_deletado = int(input('Informe o numero do item a ser deletado: ')) - 1

        if item_a_ser_deletado >= 0 and item_a_ser_deletado < len(lista_compras):
                item_deletado = lista_compras.pop(item_a_ser_deletado)
                print(f'O item {item_a_ser_deletado} foi removido. ')
        else:
            print(f'Numero invalido')

    else:
        print('Valor invalido! Informe o valor correto. ')
        continue