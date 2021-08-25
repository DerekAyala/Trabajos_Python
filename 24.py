if __name__ == "__main__":
    num:int=4
    c:int=0
    while True:
        intento:int=int(input("Ingresa un numero: "))
        if intento==num:
            print("Le atinaste")
            break
        else:
            c=c+1
        if c>=3:
            print("Fallaste")
            break
