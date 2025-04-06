#while e continue
#break quebra a repeticao e para
#continue nao executa o bloco, ele pula a iteracao

contador = 0

while contador <= 100:
    contador+=1

    if contador == 6:
        print('Nao vou mostrar o 6')
        continue

    if contador >= 10 and contador <= 27:
        continue

    print(contador)

    if contador == 40:
        break

print('Acabou')