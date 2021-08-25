if __name__ == "__main__":
    suma:int=0
    ini:int=5
    fin:int=15
    while True:
        suma=suma+ ini
        ini=ini+2
        if fin<ini:
            break
    print(suma)
    