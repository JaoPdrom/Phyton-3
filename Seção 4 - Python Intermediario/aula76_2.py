#metodos uteis dos dicionarios
import copy

pessoa = {
    'nome': 'Pedro',
    'Sobrenome': 'Missiagia',
}

#len - retorna a quantidade de chaves
print('Qtd chaves: ', len(pessoa))
print(5*'-')

#keys - retorna as chaves
print('Chaves: ', list(pessoa.keys()))
print(5*'-')

#values - retorna os valores
print('Valores: ', list(pessoa.values()))
for valor in pessoa:
    print(valor)
print(5*'-')

#items - retorna as chaves e os valores
print('Chaves e valores: ', list(pessoa.items()))
print(5*'-')

#setdefault - adiciona valor se a chave nao existe
pessoa.setdefault('idade', None)
print(pessoa['idade'])
print(5*'-')

#copy - retorna uma copia rasa (shallow copy)
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [1,2,3],
}
d2 = d1.copy() #tudo que for imutavel, sera copiado

d2['c1'] = 1000
d2['l1'][1] = 9999
print('Shallow copy: ', d1)
print('Shallow copy: ', d2)

d2 = copy.deepcopy(d1) #copia "profunda" copia todos os valores, afeta mutaveis
print('Deep copy: ', d1)
print('Deep copy: ', d2)
print(5*'-')

#get - retorna uma chave
print('Retorna a chave', pessoa.get('nome'))
print(5*'-')

#update - atualiza um dict com outro
pessoa.update({
    'nome': 'novo valor', #atualiza valor existente
    'altura': 190, #cria nova chave e valor
}) 
print('Update: ', pessoa)
pessoa.update(nome='valorrrr', idade=90)
print('Update: ', pessoa)

tupla = ('nome', 'novo valor mais top'), ('idade', 30)
pessoa.update(tupla)
print('Update com tupla: ', pessoa)

print(5*'-')

#popitem - apaga o ultimo item adicionado
ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)
print(5*'-')

#pop - apaga um item com a chave espeficicada
nome = pessoa.pop('nome')
print(nome)
print(pessoa)
print(5*'-')