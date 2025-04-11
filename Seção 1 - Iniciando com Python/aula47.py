"""
Faça um jogo para o usuario adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade
para o usuario digitar uma letra.
- Quando o usuario digitar uma letra, você vai conferir se a letra digitada
está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra.
    - Se a letra nao estiver na palavra secreta; exiba *.
Faça uma contagem de tentativas do seu usuário
"""
import os

palavra_secreta = 'carro'
letras_acertadas = ''
tamanho_palavra_secreta = len(palavra_secreta)
tentativas = 0

while True:
    

    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    #verifica se digitou uma letra
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
        continue

    #salva as letras acertadas pelo usuario em uma variavel
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    #verifica se a letra digita esta na palavra secreta
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print('Palavra formada: ', palavra_formada)
    
    #verifica se a palavra formada é igual a secreta, se for aparesenta 'Parabens' e zera as variaveis
    #se não for, ele retorna o loop e soma uma tentativa
    if palavra_formada == palavra_secreta:
        os.system('cls') #executa um comando para limpar o terminal
        print('Parabens! Palavra descoberta!')
        print(f'A palavra era: {palavra_secreta}')
        print(f'Tentativas {tentativas}')
        letras_acertadas = ''
        tentativas = 0
        
