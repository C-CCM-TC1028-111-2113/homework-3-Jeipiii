
def main():
    #escribe tu código abajo de esta línea
    albanene = int(input("Dame el numero de pliegos de papel albanene : "))
    plumones = int(input("Dame el numero de plumones : "))

    def tarjetas():
        alba = albanene * 12
        plu = plumones * 35
        tot_tar = (alba + plu)/35
        return tot_tar
    print(" El numero de tarjetas alcanza para :" + str(tarjetas()))
    pass

if __name__=='__main__':
    main()
