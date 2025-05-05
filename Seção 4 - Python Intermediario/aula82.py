#def para lambda

def executa(funcao, *args):
    return funcao(*args)
exec = lambda funcao, *args: funcao(*args)

def soma(x, y):
    return x + y
soma2 = lambda x, y: x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


print(executa(
    lambda x, y: x + y, 2, 4
))

duplica = executa(
    lambda m: lambda n: n * m, 2
)
print(duplica(2))