#lista de listas

salas = [
    #0            1
    ['Maria', 'Helena',], #0
    
    #0
    ['Elaine',], #1

    #0          1        2
    ['Luiz', 'Joao', 'Eduardo', (0, 1, 2, 3, 4)], #2 
]

# print(salas) #mostra todas as listas
# print(salas[0]) #mostra toda a lista especifica
# print(salas[0][1]) #salas[desejada][elemento_da_lista] 
# print(salas[2][3][3]) #salas[lista_desejada][elemento_lista][elemento_especifico]

#mostra os elementos das listas
for sala in salas: #percorre a lista de sala
    for aluno in sala: #recebe os valores na lista sala
        print(aluno)