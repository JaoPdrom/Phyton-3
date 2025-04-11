# exercicio: escrever um codigo que receba do input de int 
# e verifique qual numero eh maior que o outro

primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite outro valor: '))


if primeiro_valor > segundo_valor:
    print(f'O {primeiro_valor=} eh maior que o {segundo_valor=}')
elif segundo_valor > primeiro_valor:
    print(f'O {segundo_valor=} eh maior que o {primeiro_valor=}')
else:
    print(f'{primeiro_valor=} e {segundo_valor=} sao iguais ')
