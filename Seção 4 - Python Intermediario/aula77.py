# Exercício - sistema de perguntas e respostas
# 

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0

for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opcoes']
    for i, opcao in enumerate(opcoes): #enumera as opcoes
        print(f'{i}) {opcao}')
    print()

    alternativa = input('Informe a alternativa: ')

    #variaveis de controles
    acerto = False #inicia como falso a cada iteracao
    alternativa_int = None #reseta o valor a cada interacao
    qtd_alternativas = len('Opcoes') #recebe o tamanho da lista

    if alternativa.isdigit(): #verifica se a alternativa digitada eh apenas numeros
        alternativa_int = int(alternativa)

    if alternativa_int is not None: #verfica se alternativa eh nao valor
        if alternativa_int >=0 and alternativa_int < qtd_alternativas: #verifica se a altertiva esta no intervalo
            if opcoes[alternativa_int] == pergunta['Resposta']: #verifica se a alternativa eh a resposta correta
                acerto = True
    
    print()

    if acerto:
        qtd_acertos += 1
        print('Acertou!')
    else:
        print('Errou')
    print()

print(f'Voce acertou: {qtd_acertos} de {len(perguntas)}')
        
