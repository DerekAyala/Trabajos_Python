if __name__ == "__main__":
    b:int=int(input("Ingresa la base menor: "))
    while b<0:
        b:int=int(input("Ingresa la base menor: "))
    B:int=int(input("Ingresa la base mayor: "))
    while B<b:
        B:int=int(input("Ingresa la base mayor: "))
    h:int=int(input("Ingresa la altura: "))
    while h<0:
        h:int=int(input("Ingresa la altura: "))
    l:int=int(input("Ingresa la medida de un lado: "))
    while l<0:
        l:int=int(input("Ingresa la medida de un lado: "))
    print(f"El area es : {(h*(b*B))/2}")
    print(f"perimetro es : {B+b+l+l}")