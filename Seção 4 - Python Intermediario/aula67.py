#valores padroes

def soma(x, y, z=None): #z pode ou nao pode ser enviado
    if z is not None:
        print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x+y+z)
    else:
        print(f'{x=} {y=}', '|', 'x + y + z = ', x+y)


soma(1, 2)
soma(1, 2, 90)