if __name__ == "__main__":
    c:int=0
    i:int=1
    suma:int=0
    while True:
        n:int=int(input("Ingresa el limite: "))
        if n>0:
            break
    while True:
        suma=suma+((2*i))
        i=i+1
        c=c+1
        if c>=n:
            break
    print(suma)