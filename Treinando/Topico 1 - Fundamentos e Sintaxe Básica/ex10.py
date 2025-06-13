'''
Baseado no exercício anterior, use as variáveis de altura e peso para 
calcular o IMC do usuário. A fórmula do IMC é: **peso / (altura * altura)**.

Exiba o resultado do IMC para o usuário com uma mensagem clara, por exemplo: "Seu IMC é de X.XX".

O que praticar:
Reutilização de variáveis, input(), casting, e a aplicação de uma fórmula matemática 
que envolve exponenciação ou multiplicação, e formatação do resultado final.
'''

altura = float(input('Informe a sua altura: '))
peso = float(input('Informe o seu peso: '))

imc = peso/(altura*altura)

print(f'Seu IMC e de {imc}')