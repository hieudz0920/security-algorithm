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
k = 0 
q = 0
p = 0
s = 0
a = []
b = []
for i in range(1, n + 1):
    if n % i == 0:
        a.append(i)
        p += i
        s += 1
for j in a:
    if ktnt(j) :
        q += j
        k += 1
result = n + p + s - q - k
print(result)


