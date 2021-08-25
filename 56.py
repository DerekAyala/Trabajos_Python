if __name__ == "__main__":
    c:int=3
    while True:
        n:int=int(input("Cuantos numeros deseas conocer: "))
        if n > 0:
            break
    for i in range(0,n):
        print(c)
        c=c*3