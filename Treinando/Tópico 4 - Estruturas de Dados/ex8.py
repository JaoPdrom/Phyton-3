'''
Dadas duas listas de alunos que participaram de dois projetos diferentes:

projeto_A = ['Ana', 'Bruno', 'Carla', 'Daniel']
projeto_B = ['Bruno', 'Daniel', 'Eva', 'Felipe']

Use conjuntos (set) para encontrar e exibir quais alunos participaram de AMBOS os projetos.

O que praticar:
Operação de interseção (&) de conjuntos.
'''

projeto_A = ['Ana', 'Bruno', 'Carla', 'Daniel']
projeto_B = ['Bruno', 'Daniel', 'Eva', 'Felipe']

print('Alunos que estao em ambos projetos: ', set(projeto_A) & set(projeto_B))