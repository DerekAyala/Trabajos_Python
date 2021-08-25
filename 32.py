def calificacion(ca:int):
    if ca > 9:
        print("A")
    if ca <= 9 and ca >= 8 :
        print("B")
    if ca < 8 and ca >= 6 :
        print("C")
    if ca < 6 :
        print("D")
if __name__ == "__main__":
    suma1:int=0
    suma2:int=0
    c:int=0
    i:int=0
    b:int=0
    while True:

        while True:
            ca:int=int(input("Ingresa una calificaion: "))
            if ca>0 and ca <= 10:
                break
        calificacion(ca)
        c=c+1
        suma1=suma1+ca
        if ca >= 6:
            i=i+1
            suma2=suma2+ca
        else:
            b=b+1
        n:int=int(input("Si deseas ingresar otra calificacion ingresa 1: "))
        if n != 1:
            break
    print(f"El promedio del grupo fue {suma1/c}")
    print(f"reprobados {b}")
    print(f"aprobados {i}")
    calificacion(suma2/i)
    print("D")
    