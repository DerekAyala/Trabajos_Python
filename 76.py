if __name__ == "__main__":
    c:int=0
    i:int=1
    suma:int=1
    n:int=int(input("Ingresa el limite: "))
    while n<0:
        n:int=int(input("Ingresa el limite: "))
    while c<n:
        suma=suma*((2*i)+1)
        i=i+1
        c=c+1
    print(suma)