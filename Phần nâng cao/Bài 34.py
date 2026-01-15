import random
def nhanbinhphuongcolap(a, k, n):
    ds_k = []
    while k > 0:
        r = k % 2
        ds_k.append(r)
        k = int(k // 2)
    A = a
    if ds_k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(ds_k)):
        A = (A*A) % n 
        if ds_k[i] == 1:
            b = (A*b) % n
    return b

def fermat(n, t):
    for _ in range(t):
        a = random.randint(2, n - 2)
        b= nhanbinhphuongcolap(a, n -1, n)
        if b != 1:
            return ("Hop so")
    return ("Nguyen to")

while True:
        try:
            n = int(input("Nhap n: "))
            if n < 3 or n % 2 == 0:
                raise ValueError("Nhap lai n")
            break
        except ValueError as r:
            print(r)

try:
        t = int(input("Nhap so lan thu: "))
except ValueError:
        print("Hay nhap so nguyen")

print(fermat(n, t))  
