if __name__ == "__main__":
    a_ana:int=int(input("Ingresa tu año de nacimiento: "))
    while a_ana<1900:
        a_ana:int=int(input("Ingresa tu año de nacimiento: "))
    a_ac:int=int(input("Ingresa el año actual: "))
    while a_ac<a_ana:
        a_ac:int=int(input("Ingresa el año actual: "))
    print(f"tu edad es {a_ac-a_ana}")