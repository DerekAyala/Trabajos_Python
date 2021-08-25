if __name__ == "__main__":
    suma:int=0
    while True:
        n:int=int(input("Ingresa el limite: "))
        if n>0:
            break
    for i in range(1,n+1):
        suma=suma+((2*i))
    print(suma)