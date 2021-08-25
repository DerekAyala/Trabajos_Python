if __name__ == "__main__":
    n:int=int(input("Ingresa el numero de lados: "))
    while n < 5 or n > 12:
        n:int=int(input("Ingresa el numero de lados: "))
    l:int=int(input("Ingresa la medida de los lados: "))
    while l<0:
        l:int=int(input("Ingresa la medida de los lados: "))
    a:int=int(input("Ingresa el aponema: "))
    while a < 0:
        a:int=int(input("Ingresa el aponema: "))
    p:int=l*n
    print(p)
    print(p*a)