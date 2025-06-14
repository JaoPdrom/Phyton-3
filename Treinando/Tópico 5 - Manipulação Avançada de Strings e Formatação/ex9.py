'''
Imagine uma linha de log no formato: "INFO:2023-10-27:Usuário 'admin' logou com sucesso."
Crie um programa que receba essa string e extraia:

1. O nível do log (INFO).
2. A data (2023-10-27).
3. A mensagem ("Usuário 'admin' logou com sucesso.").\
Exiba cada uma dessas partes separadamente.
    
O que praticar:
Combinação de .split() com delimitadores diferentes e o parâmetro maxsplit para controlar o número de divisões.
'''

log = "INFO:2023-10-27:Usuário 'admin' logou com sucesso."
log_split = log.split(':')

nivel_log = log_split[0]
data_log = log_split[1]
mensagem_log = log_split[2]

print('Nível do log:', nivel_log)
print('Data do log:', data_log)
print('Mensagem do log:', mensagem_log)