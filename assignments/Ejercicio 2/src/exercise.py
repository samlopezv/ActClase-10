

def equivalente (hrs,minu,seg):

    tot = (hrs*60*60)+(minu*60)+ seg

    return tot


def tiemp (proceso):
    print(proceso)
    hrs = int(input('¿Cuántas horas del ' + proceso+'?'))
    minu = int(input('¿Cuántos minutos del ' +proceso+'?'))
    seg = int(input('¿Cuántos segundos del ' +proceso+ '?'))

    print('Total de segundos del proceso' + proceso+' ='+ str(equivalente(hrs, minu, seg)))


def main():
    #escribe tu código abajo de esta línea
    tiemp('proceso-1')
    tiemp('proceso-2')


if __name__=='__main__':
    main()
