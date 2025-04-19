#argumentos nomeados e nao nomeados 
#parametro vai na funcao
#argumento sao os valores

def soma(x, y): #(x, y) sao parametros
    print(f'{x=} {y=}', '|', 'x + y = ', x+y)

#funcao nao tem retorno, rotorna None
print(soma(1,2))

soma(1,2) #(1, 2) sao argumentos
soma(y=2, x=1) #se um argumento eh nomeado, todos os proximos precisam ser nomeados
