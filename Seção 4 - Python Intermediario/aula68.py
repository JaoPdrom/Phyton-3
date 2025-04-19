#escopo de funcoes em python

x = 1

def escopo():
    global x #manipula o X definido fora da funcao
    x = 10

    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)