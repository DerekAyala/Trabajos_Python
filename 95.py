if __name__ == "__main__":
    while True:
        d:int=int(input("Ingresa la diagonal menor: "))
        if d>0:
            break
    while True:
        D:int=int(input("Ingresa la diagonal mayor: "))
        if D>d:
            break
    while True:
        l:int=int(input("Ingresa un lado: "))
        if l>0:
            break
    print(f"El area es : {d*D}")
    print(f"El perimetro es: {l+l+l+l}")
    
        