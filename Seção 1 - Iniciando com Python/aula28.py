"""
exercicio
peça para o usuario digitar seu nome e idade
se o nome e a idade forem digitados exiba:
    seu nome é {nome}
    seu nome invertido é {nome invertido}
    se nome contem (ou nao) espaços
    seu nome tem {n} letras
    a primeira letra do seu nome é {letra}
    a ultima letra do seu nome é {letra}
se nada for digitado em nome ou idade exiba:
    "desculpe, mas deixou campos vazios"
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if (nome and idade) != '':
    print(f'Seu nome eh {nome}') #exibe o nome
    print(f'Seu nome invertido eh {nome[::-1]}') #exibe o nome invertido
    
    if (' ' in nome): #contem ou nao espacos
        print('Seu nome contem espacos')
    else:
        print('Seu nome nao contem espacos')

    print(f'Seu nome tem {len(nome)}') #exibe a quantidade de caracteres
    print(f'A primeira letra do seu nome eh {nome[0]}') #exibe a primeira letra do nome
    print(f'A ultima letra do seu nome eh {nome[len(nome)-1]}') #exibe a ultima letra do nome
else:
    print('Desculpe, voce deixou campos vazios')
