import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
def tinh(m, l, a, b, c):
    for x in range(m, l + 1):
        d = a * x * x + b * x + c
        if ktnt(d):
            return d, x
    return None


while True:
    try:
        m = int(input("Nhap m: "))
        l = int(input("Nhap l: "))
        if m <=0 or l <=m :
            raise ValueError("Nhap lai ")
        break
    except ValueError as z:
        print(z)
a = int(input("Nhap A: "))
b = int(input("Nhap B: "))
c = int(input("Nhap C: "))
result = tinh(m, l, a, b, c)
if result != None:
    print(f"x = {result[1]}")
    print(f"Gia tri bieu thuc la so nguyen to: {result[0]}")
else:
    print("Khong co gia tri cua x")