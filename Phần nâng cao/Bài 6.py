while True:
    try:
        n = int(input("Nhap N: "))
        if n <=0:
            raise ValueError("Nhap lai N")
        break
    except ValueError as z:
        print(z)
c = []
for a in range(1, n):
    b = 0
    for i in range(1, a):
        if a % i == 0:
            b += i

            d = 0 
            for j in range(1, b):
                if b % j == 0:
                    d += j
                    if d == a and a < b:
                        c = [a, b]
f = []
if c == f:
    print(f"Khong co cap so than thiet nao nho hon {n}")
else:
    print(f"Cap so than thiet nho hon {n} la {c}")


