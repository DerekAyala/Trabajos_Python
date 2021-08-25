if __name__ == "__main__":
    l:int=int(input("Ingresa el lado: "))
    while l<0:
        l:int=int(input("Ingresa el lado: "))
    a:int=int(input("Ingresa el apotema: "))
    while a<0:
        a:int=int(input("Ingresa el apotema: "))
    print(f"el area es: {(l*5)*a}")
    print(f"el perimetro es :{l*5}")