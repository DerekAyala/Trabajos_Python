if __name__ == "__main__":
    c:int=0
    ini:int=10
    fin:int=56
    while True:
        ini=ini+2
        c=c+1
        if ini >= fin:
            break
    print(c)