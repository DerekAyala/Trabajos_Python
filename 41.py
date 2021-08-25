if __name__ == "__main__":
    b:int=int(input("Ingresa la base: "))
    while b<0:
        b:int=int(input("Ingresa la base: "))   
    h:int=int(input("Ingresa la altura: "))
    while h<0:
        h:int=int(input("Ingresa la altura: "))
    print((b*h)/2)
    print(b+b+h+h)