import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

def triple(n):
    for i in range(n):
        if i * i * i == n:
            return True
    return False

for i in range(100, 1000):
    if ktnt(i):
        k = int(str(i)[::-1])
        if triple(k):
            print(i)
