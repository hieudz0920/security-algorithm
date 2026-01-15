import math
import random
def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True
def num_random(n, list_random):
    for i in range(n):
        list_random.append(int(random.random() * 100))

def result(list_random):
    list_primre = []
    for i in list_random:
        if prime(i):
            list_primre.append(i)
    return list_primre

while True:
    try:
        n = int(input("Nhap N: "))
        if n <=0:
            raise ValueError("Nhap lai N")
        break
    except ValueError as z:
        print(z)

list_random = []
num_random(n, list_random)
print(f"Mang ngau nhien kich thuoc {n} la: {list_random} ")
print(f"So nguyen to cua mang tren la: {result(list_random)} ")
