if __name__ == "__main__":
    c:int=2
    i:int=0
    n:int=int(input("Cuantos numeros deseas conocer: "))
    while n<0:
        n:int=int(input("Cuantos numeros deseas conocer: "))
    while i < n:
        print(c)
        c=c*2
        i=i+1