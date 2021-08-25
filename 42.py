if __name__ == "__main__":
    i:int=0
    c:int=0
    while True:
        n:int=int(input("Ingresa la cantidad de numeros a imprimir: "))
        if n > 0:
            break
    while True:
        if i == 0:
            print(i)
            i=i+1
        else:
            print(i)
            i=i-1
        c=c+1
        if c  >= n:
            break
