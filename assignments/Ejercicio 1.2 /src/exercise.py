

def equivalente (hrs,min,seg):

    tot = (hrs*60*60)+(min*60)+ seg

    return tot


def main():
    #escribe tu código abajo de esta línea
    a = equivalente(2,20,8)
    print(a)


if __name__=='__main__':
    main()
