if __name__ == "__main__":
    pi:int=3.1416
    while True:
        r:int=int(input("Ingresa el radio: "))
        if r >0:
            break
    print(f"El area es : {pi*(r**2)}")
    print(f"la circuferencia es : {pi*(r*2)}")