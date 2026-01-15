import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

def binh_phuong(n):
    for i in range(1, n):
        for j in range(1, n):
            if i * i + j * j == n and i < j:
                return True
    return False


while True:
    try:
        a = int(input("Nhap A: "))
        b = int(input("Nhap B: "))
        if a < 0 or b < a:
            raise ValueError("Nhap lai")
        break
    except ValueError as z:
        print(z)

for i in range(a, b + 1):
    if ktnt(i):
        dem = 0
        if binh_phuong(i):
            dem += 1

print(dem)
