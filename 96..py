if __name__ == "__main__":
    d:int=int(input("Ingresa la diagonal menor: "))
    while d<0:
        d:int=int(input("Ingresa la diagonal menor: "))
    D:int=int(input("Ingresa la diagonal mayor: "))
    while D<d:
        D:int=int(input("Ingresa la diagonal mayor: "))
    l:int=int(input("Ingresa un lado: "))
    while l<0:
        l:int=int(input("Ingresa un lado: "))
    print(f"El area es : {d*D}")
    print(f"El perimetro es: {l+l+l+l}")