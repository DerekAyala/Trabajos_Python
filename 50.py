if __name__ == "__main__":
    c:int=3
    n:int=int(input("Cuantos numeros deseas conocer: "))
    while n<0:
        n:int=int(input("Cuantos numeros deseas conocer: "))
    for i in range(0,n):
        print(c)
        c=c+5