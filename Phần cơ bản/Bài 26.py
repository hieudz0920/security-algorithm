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
        if n <= 0 or n >= 10000:
            raise ValueError("Nhap lai N")
        break
    except ValueError as z:
        print(z) 


a = []
for x in range(1, n):
    for i in range(1, x):
        if ktnt(i):
            if x % i == 0 and x % (i*i) == 0:
                a.append(x)
print(f"Cac so manh me nho hon {n}: {a}")

