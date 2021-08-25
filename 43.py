if __name__ == "__main__":
    i:int=0
    c:int=0
    n:int=int(input("Ingresa la cantidad de numeros a imprimir: "))
    while n < 0:
        n:int=int(input("Ingresa la cantidad de numeros a imprimir: "))
    while c < n:
        if i == 0:
            print(i)
            i=i+1
        else:
            print(i)
            i=i-1
        c=c+1
        