if __name__ == "__main__":
    n:int=int(input("ingresa un numero: "))
    while(n<=0):
        n:int=int(input("ingresa un numero: "))
    c:int=1
    while(c<=5):
        print(f"{n} x {c} = {n*c}")
        c=c+1
    