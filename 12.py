if __name__ == "__main__":
    while True:
        a_ana:int=int(input("Ingresa tu año de nacimiento: "))
        if a_ana>1900:
            break
    while True:
        a_ac:int=int(input("Ingresa el año actual: "))
        if a_ac>a_ana:
            break
    print(f"tu edad es {a_ac-a_ana}")