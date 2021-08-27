
def main():
    #escribe tu código abajo de esta línea
    año =int(input("Dame el valor de un año : "))
    def es_bisiesto(año):
        if año % 4 == 0:
            True
        elif año % 100 == 0:
            False
        else:
            False

    print(es_bisiesto(año)) 
    pass

if __name__=='__main__':
    main()
