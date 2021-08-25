if __name__ == "__main__":
    while True:
        b:int=int(input("Ingresa la base menor: "))
        if b>0:
            break
    while True:
        B:int=int(input("Ingresa la base mayor: "))
        if B>b:
            break
    while True:
        h:int=int(input("Ingresa la altura: "))
        if h>0:
            break
    while True:
        l:int=int(input("Ingresa la medida de un lado: "))
        if l>0:
            break
    print(f"El area es : {(h*(b*B))/2}")
    print(f"perimetro es : {B+b+l+l}")