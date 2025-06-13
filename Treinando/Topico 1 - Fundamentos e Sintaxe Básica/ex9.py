'''
Crie um programa que colete as seguintes informações do usuário em variáveis separadas:

1. Primeiro Nome (str)
2. Sobrenome (str)
3. Idade (int)
4. Altura em metros (float)
5. Peso em quilogramas (float)

Após coletar todos os dados, exiba um "Resumo do Perfil" formatado, mostrando 
todas as informações de forma organizada em várias linhas.

O que praticar:
Gerenciamento de múltiplas variáveis com diferentes tipos, múltiplos input(), 
múltiplos castings e formatação de uma saída com print() mais complexa.
'''

primeiro_nome = str(input('Informe seu primeiro nome: '))
sobrenome = str(input('Informe seu sobrenome: '))
idade = int(input('Informe a sua idade: '))
altura = float(input('Informe a sua altura: '))
peso = float(input('Informe seu peso: '))

print(
    f'Bem-vindo {primeiro_nome} {sobrenome}\nVoce tem {idade} anos \n{altura} de altura \nPesa {peso}'
)