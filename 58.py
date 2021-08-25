if __name__ == "__main__":
    c:int=1
    s:int=2
    i:int=0
    n:int=int(input("Cuantos numeros deseas conocer: "))
    while n < 0:
        n:int=int(input("Cuantos numeros deseas conocer: "))
    while i< n:
        print(c)
        c=c+s
        s=s+1
        i=i+1
        