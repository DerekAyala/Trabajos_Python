if __name__ == "__main__":
    while True:
        n:int=int(input("Ingresa el numero de lados: "))
        if n >= 5 and n <= 12:
            break
    while True:
        l:int=int(input("Ingresa la medida de los lados: "))
        if l>0:
            break
    while True:
        a:int=int(input("Ingresa el aponema: "))
        if a > 0:
            break
    p:int=l*n
    print(p)
    print(p*a)