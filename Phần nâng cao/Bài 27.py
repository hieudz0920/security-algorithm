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
c = []
for a in range(1, 1000):
    for b in range(1, 1000):
        if ktnt(gcd(a, b)) and a < b:
            c.append((a, b))
for d in c:
    print(d)


        
        