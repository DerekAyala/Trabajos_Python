if __name__ == "__main__":
    suma:int=1
    mul:int=0
    i:int=1
    c:int=0
    while True:
        x:int=int(input("Ingresa la base: "))
        if x > 0:
            break
    while True:
        n:int=int(input("Ingresa el limite: "))
        if n>0:
            break
    for c in range(1,n+1):
        mul=x*i
        print(f"{x} x {i} = {mul}")
        i=i+1
        suma=suma*mul
    print(suma)