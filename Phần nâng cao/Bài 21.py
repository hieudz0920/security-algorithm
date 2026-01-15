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
        a = int(input("Nhap A: "))
        b = int(input("Nhap B: "))
        if a < 0 or b < a:
            raise ValueError("Nhap lai")
        break
    except ValueError as z:
        print(z)
c = []
for i in range(a, b + 1):
    dem = 0
    for j in range(1, i):
        if ktnt(j):
            dem += 1
    if ktnt(dem):
        c.append(i)
print(f"Co {len(c)} sieu so nguyen to")