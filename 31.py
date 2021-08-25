if __name__ == "__main__":
    ici_h:int=0
    ici_m:int=0
    im_h:int=0
    im_m:int=0
    ime_h:int=0
    ime_m:int=0
    iset_h:int=0
    iset_m:int=0
    isc_h:int=0
    isc_m:int=0
    n:int=1
    while n == 1:
        sex:int=int(input("1. hombre y 2.mujer: "))
        while sex != 1 and sex != 2:
            sex:int=int(input("1. hombre y 2.mujer: "))
        if sex == 1:
            car:int=int(input("Que carrera perteneces : 1.ici   2.im    3.ime   4.iset  5.isc: "))
            while car != 1 and car != 2 and car != 3 and car != 4 and car != 5:
                car:int=int(input("Que carrera perteneces : 1.ici   2.im    3.ime   4.iset  5.isc: "))
            if car == 1:
                ici_h=ici_h+1
            if car == 2:
                im_h=im_h+1
            if car == 3:
                ime_h=ime_h+1
            if car == 4:
                iset_h=iset_h+1
            if car==5:
                isc_h=isc_h+1
        if sex == 2:
            car:int=int(input("Que carrera perteneces : 1.ici   2.im    3.ime   4.iset  5.isc: "))
            while car != 1 and car != 2 and car != 3 and car != 4 and car != 5:
                car:int=int(input("Que carrera perteneces : 1.ici   2.im    3.ime   4.iset  5.isc: "))
            if car == 1:
                ici_m=ici_m+1
            if car == 2:
                im_m=im_m+1
            if car == 3:
                ime_m=ime_m+1
            if car == 4:
                iset_m=iset_m+1
            if car == 5:
                isc_m=isc_m+1
        n:int=int(input("si quieres ingresar otro estudiante ingresa 1: "))
    print(f"Ici  hombres : {ici_h}  mujeres: {ici_m }    Im  hombre: {im_h}  mujeres: {im_m}  Ime   hombre: {ime_h}  mujeres: {ime_m}   Iset   hombres: {iset_h}  mujeres: {iset_m}  Isc    hombres: { isc_h}  mujeres: { isc_m} ")