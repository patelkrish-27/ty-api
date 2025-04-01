def toh(n, source,aux,dest):
    if n == 1:
        print(f'Move disk 1 from rod {source} to rod {dest}')
        return
    toh(n-1,source,dest,aux)
    print(f'Move disk {n} from rod {source} to rod {dest}')
    
    toh(n-1,aux,source,dest)

n =3
toh(n,"A","B","C")