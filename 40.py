if __name__ == "__main__":
    while True:
        b:int=int(input("Ingresa la base: "))
        if b > 0:
            break
    while True:
        h:int=int(input("Ingresa la altura: "))
        if h > 0:
            break
    print((b*h)/2)
    print(b+b+h+h)