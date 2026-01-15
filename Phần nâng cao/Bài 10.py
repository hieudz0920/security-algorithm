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
        if n <=0:
            raise ValueError("Nhap lai N")
        break
    except ValueError as z:
        print(z)

a = []
dem_uoc = 0
dem_nt = 0

for i in range(1, n + 1):
    if n % i:
        a.append(i)
        dem_uoc += 1

for j in a:
    if ktnt(j):
        dem_nt += 1

print(f"So uoc cua N la: {dem_uoc}")
print(f"So uoc nguyen to cua N la: {dem_nt}")