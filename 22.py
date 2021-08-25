if __name__ == "__main__":
    suma:int=0
    c:int=0
    while True:
        n:int=int(input("Ingresa la cantidad de numeros a meter: "))
        if n>0:
            break
    while True:
        num:int=int(input("Ingresa un numero:"))
        if num>0:
            suma=suma+num
            c=c+1
        if c>=n:
            break
    print(suma/c)
    