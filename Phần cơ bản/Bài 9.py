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
        n = int(input("Nhap N: "))
        if n <= 0 :
            raise ValueError("Nhap lai N")
        break
    except ValueError as z:
        print(z)

dem = 0
for i in range(1, n+1):
    if ktnt(i):
        dem += 1

print(f"So so nguyen to nho hon hon hoac bang N la {dem}")

