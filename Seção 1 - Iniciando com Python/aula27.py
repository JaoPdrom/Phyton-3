#fatiamento de string
# 012345678
# olá mundo
#-987654321
#fatiamento [i:f:p] [::] inicio, fim e parte

var = 'Olá Mundo'
print(var[4]) #mostra apenas o indice 0  
print(var[2:5]) #comeca no indice 2 e vai ate o indice 5
print(var[:7]) #comeca no indice 0 e vai ate o indice 7
print(10*'-')
print(len(var)) #calcula a quantidade de caracteres
print(var[0:len(var):1]) #pega do incio da str ate o tamanho dela um por um
print(var[0:len(var):2]) #pega do incio da str ate o tamanho dela e pula um caracter
print(var[::-1]) #inverte a str