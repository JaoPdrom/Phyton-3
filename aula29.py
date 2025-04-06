#introducao ao try/except
#try - tentar executar
#execpt - ocorreu erro ao tentar executar

num_str = input('Vou dobrar o numero: ')

try:
    print('STR:', num_str)
    num_float = float(num_str)
    print('FLOAT:', num_float)
    print(f'O dobro de {num_str} eh {num_float * 2}')
except:
    print('Isso nao eh um numero')
