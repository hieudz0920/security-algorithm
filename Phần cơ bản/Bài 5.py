import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
         if n % i == 0:
            return False
    return True

while True:
    try:
        a = int(input("Nhap A: "))
        if a < 0:
            raise ValueError("Nhap lai A")
        break
    except ValueError as z:
        print(z)

while True:
    try:
        b = int(input("Nhap B: "))
        if b <= a:
            raise ValueError("Nhap lai B")
        break
    except ValueError as x:
        print(x)

tong = 0

for i in range(a, b + 1):
    if ktnt(i):
        tong += i

print(f"Tong cua cac so nguyen to nam trong khoang [{a}, {b}] la {tong}")
