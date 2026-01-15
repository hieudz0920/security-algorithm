import math
import random

def ktnt(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def random_soP():
    while True:
        p = random.randint(101, 499)
        if ktnt(p):
            return p

def random_soQ():
    while True:
        q = random.randint(101, 499)
        if ktnt(q):
            return q

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def random_soE(f):
    while True:
        e = random.randint(2, f - 1)
        if gcd(e, f) == 1:
            return e

def tinhD(a, b):
    b1 = b
    x2, x1 = 1, 0
    while b > 0:
        q = a // b
        a = b 
        b = a - q * b
        x2 = x1 
        x1 = x2 - q * x1
    if x2 < 0:
        x2 += b1
    return x2

def nhanbinhphuongcolap(a, k, n):
    ds_k = []
    while k > 0:
        r = k % 2
        ds_k.append(r)
        k = k // 2
    A = a
    b = 1
    if ds_k[0] == 1:
        b = a
    for i in range(1, len(ds_k)):
        A = (A * A) % n
        if ds_k[i] == 1:
            b = (A * b) % n
    return b

# Đảm bảo p và q là các số nguyên tố khác nhau
p = random_soP()
q = random_soQ()
while p == q:
    q = random_soQ()

n = p * q
phi_n = (p - 1) * (q - 1)
e = random_soE(phi_n)
d = tinhD(e, phi_n)

sbd = int(input("Nhập SBD: "))
m = sbd + 123

c = nhanbinhphuongcolap(m, e, n)
decoded_m = nhanbinhphuongcolap(c, d, n)

print(f"Ban ma c là: {c}")
print(f"Giá trị giải mã m là: {decoded_m}")


