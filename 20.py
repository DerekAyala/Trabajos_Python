if __name__ == "__main__":
    i:int=0
    c:int=1
    num:int=int(input("Ingresa un numero: "))
    if num>0:
        while True:
            i=i+2
            print(i)
            if 10<=i:
                break
    else:
        while True:
            print(c)
            c=c+2
            if c>15:
                break