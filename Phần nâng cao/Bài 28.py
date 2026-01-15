import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

def gcd(a, b):
    while b > 0:
        r = a % b
        a, b = b, r
    return a

def carmichael(n):
    if ktnt(n):
        return False
    for i in range(2, n):
        if gcd(i, n):
            if pow(i, n - 1, n) == 1:
                return True
    return False

while True:
    try: 
        n = int(input("Nhap N: "))
        if n < 0 or n > 10000:
            raise ValueError("Nhap lai N")
        break
    except ValueError as r:
        print(r)

result = []
d = []
for i in range(2, n):
    if carmichael(i):
        result.append(i)
if result == d:
    print("Khong co so Carmichael nao nho hon", n)
else:
    print("Cac so Carmichael nho hon", n,"la")
    for j in result:
        print(j)

        
