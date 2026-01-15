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
    if ktnt(i):
        c.append(i)
d = sum(c)
if ktnt(d):
    print("YES")
else: 
    print("NO")