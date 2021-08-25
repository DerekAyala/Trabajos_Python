if __name__ == "__main__":
    while True:
        l:int=int(input("Ingresa el lado: "))
        if l>0:
            break
    while True:
        a:int=int(input("Ingresa el apotema: "))
        if a>0:
            break
    print(f"el area es: {(l*5)*a}")
    print(f"el perimetro es :{l*5}")