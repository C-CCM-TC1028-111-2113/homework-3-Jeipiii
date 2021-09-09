
def main():
    #escribe tu código abajo de esta línea
    año =int(input("Dame el valor de un año : "))
    def es_bisiesto(año):
        if año % 4 == 0:
            True ##  NO ESTAS REGRESANDO VALORES, TIENES QUE USAR RETURN
        elif año % 100 == 0:
            False   ##  NO ESTAS REGRESANDO VALORES, TIENES QUE USAR RETURN
        else:
            False ##  NO ESTAS REGRESANDO VALORES, TIENES QUE USAR RETURN

    print(es_bisiesto(año)) 
    pass

if __name__=='__main__':
    main()
