import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

while True:
    try:
        n = int(input("Nhap N: "))
        if n < 2 or n > 10:
            raise ValueError("Hay nhap lai N")
        break
    except ValueError as z:
        print(z)

a = pow(10, n - 1)
b = pow(10, n)
c = []
for i in range(a, b):
    if ktnt(i):
        c.append(i)
print(f"Cac so nguyen to co {n} chu so la: {c}")
        
        