if __name__ == "__main__":
    num:int=4
    c:int=0
    for c in range(1,3+1):
        intento:int=int(input("Ingresa un numero: "))
        if intento==num:
            print("Le atinaste")
            break
        if intento>num:
            print("te pasaste")
        else:
            print("te falto")
        if c==3:
            print("Fallaste")