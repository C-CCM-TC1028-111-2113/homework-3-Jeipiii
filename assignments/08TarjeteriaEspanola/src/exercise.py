def total_tarjeta(albanene, plumones):
    pli_tarjetas = pliegos * 12
    plu_tarjetas = pliegos * 35
    if pli_tarjetas > plu_tarjetas :
        total_tarjeta = plu_tarjetas
    elif plu_tarjetas > pli_tarjetas:
        total_tarjeta = pli_tarjetas
    return total_tarjeta
def main ():
    pliegos = int(input("Dame la cantidad de albanene"))
    plumones  = int(input("Dame la cantidad de plumones"))
    maximo = total_tarjeta(albanene, plumones))
    print("El numero máximo de tarjetas es" (total_tarjeta))
if __name__== "__main__"
    main()
      
       
                  
