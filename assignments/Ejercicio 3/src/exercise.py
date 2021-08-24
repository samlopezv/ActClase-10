def op (a,b,c):
    if c == 's':
        return (a+b)

    elif c == 'r':
        return (a-b)

    elif c == 'm':
        return (a*b)

    elif c == 'd':
        return (a/b)

    else:
        return 'Clave incorrecta'


def main():

    a = int(input('Dame el valor del primer número: '))
    b = int(input('Dame el valor del segundo número: '))
    c = input('Ingresa la clave s(suma), r(resta), m(multiplicación), d(división): ')

    print(op(a,b,c))

if __name__=='__main__':
    main()
