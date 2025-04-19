#closure e funcoes que retornam funcoes

def saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = saudacao('bom dia')
falar_boa_noite = saudacao('boa noite')

for nome in ['Joao', 'Pedro', 'Ana']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))