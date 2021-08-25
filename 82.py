if __name__ == "__main__":
    pi:int=3.1416
    r:int=int(input("Ingresa el radio: "))
    while r<0:
        r:int=int(input("Ingresa el radio: "))
    print(f"El area es : {pi*(r**2)}")
    print(f"la circuferencia es : {pi*(r*2)}")