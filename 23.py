if __name__ == "__main__":
    suma:int=0
    c:int=0
    n:int=int(input("Ingresa la cantidad de numeros a meter: "))
    while n<0:
        n:int=int(input("Ingresa la cantidad de numeros a meter: "))
    while c<n:
        num:int=int(input("Ingresa un numero:"))
        if num>0:
            suma=suma+num
            c=c+1
    print(suma/c)
    