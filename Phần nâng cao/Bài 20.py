def gcd(a, b):
    A = a
    B = b
    while B > 0:
        r = A % B
        A, B = B, r
    return A

while True:
    try:
        m = int(input("Nhap m: "))
        n = int(input("Nhap n: "))
        d = int(input("Nhap d: "))
        if m <= 0 or m >= n or n >= 1000 or d>= 1000 :
            raise ValueError("Nhap lai ")
        break
        
    except ValueError as z:
        print(z)

for i in range(m, n + 1):
    for j in range(m , n + 1):
        if gcd(i,j) == d and i < j:
            a = [i, j]
            print(a)

