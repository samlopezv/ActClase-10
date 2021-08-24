
def areaRec (l, a):
    area = l*a
    return area

def perimetroRec (l,a):
    perimetro = 2*(l+a)
    return perimetro

def main():
    l = float(input('Dame el valor del largo : '))
    a = float(input('Dame el valor del ancho: '))
    r = input('¿Qué deseas conocer a(área) o p(perímetro)? ')

    if r == 'a':
        print('El área es: ' + str(areaRec(l,a)))

    elif r == 'p':
        print('El perimetro es: ' + str(perimetroRec(l,a)))

    else :
        print('Respuesta incorrecta')

if __name__=='__main__':
    main()
