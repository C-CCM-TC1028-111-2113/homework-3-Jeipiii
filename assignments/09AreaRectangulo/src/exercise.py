
def main():
    #escribe tu código abajo de esta línea
    base = int(input("Dame la base: "))
    altura = int(input("Dame la altura: "))

    def area():
        area_1 = base * altura
        return area_1
    print("El area es : " + str(area()))    
    pass

if __name__=='__main__':
    main()
