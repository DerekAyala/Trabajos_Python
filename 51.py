if __name__ == "__main__":
    c:int=2
    i:int=0
    while True:
        n:int=int(input("Cuantos numeros deseas conocer: "))
        if n > 0:
            break
    while True:
        print(c)
        c=c*2
        i=i+1
        if i >= n:
            break