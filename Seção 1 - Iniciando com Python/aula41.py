#while else
#else so eh executado quando o while for finalizado

string = 'valorqualquer'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i += 1
else:
    print('O else foi executado.')
print('Fora do bloco while.')