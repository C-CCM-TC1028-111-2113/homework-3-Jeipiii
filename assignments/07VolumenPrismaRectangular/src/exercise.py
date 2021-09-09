
def main():
    #escribe tu código abajo de esta línea
    base = int(input("Da un valor para la base : ")) ##Debían ser float
    altura = int(input("Da un valor para la altura : ")) ##Debían ser float
    profundidad = float(input("Da un valor para la profundidad" )) ##Debían ser float
           
    def area():
        area_1 = base * altura
        volumen = area_1 * profundidad
        return volumen
    print("El volumen del prisma es : "+ str(area()))
    pass

if __name__=='__main__':
    main()
