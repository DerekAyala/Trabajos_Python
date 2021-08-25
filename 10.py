if __name__ == "__main__":
    while True:
        n:int=int(input("ingresa un numero: "))
        if n>0:
            break
    c:int=1
    while True:
        print(f"{n} x {c} = {n*c}")
        c=c+1
        if c>5:
            break