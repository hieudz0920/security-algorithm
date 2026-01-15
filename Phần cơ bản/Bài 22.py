import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
def fifj(n):
    if ktnt(n):
        d = n
    else:
        d = 0
    return d

while True:
    try:
        l = int(input("Nhap L: "))
        r = int(input("Nhap R: "))
        if l < 0 or r < l:
            raise ValueError("Nhap lai")
        break
    except ValueError as z:
        print(z)

a = []
for i in range(l ,r + 1):
    for j in range(l, r + 1):
        if j > i:
            result = fifj(i) * fifj(j)
            a.append(result)
print(f"Ket qua la: {sum(a)}")
