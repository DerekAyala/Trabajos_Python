if __name__ == "__main__":
    suma:int=1
    mul:int=0
    i:int=1
    c:int=0
    x:int=int(input("Ingresa la base: "))
    while x < 0:
        x:int=int(input("Ingresa la base: "))
    n:int=int(input("Ingresa el limite: "))
    while n<0:
        n:int=int(input("Ingresa el limite: "))
    while c<n:
        mul=x*i
        print(f"{x} x {i} = {mul}")
        i=i+1
        suma=suma*mul
        c=c+1
    print(suma)