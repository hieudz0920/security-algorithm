#Họ và tên: Nguyễn Huy Hiệu
#Mã SV: AT190522
import math
def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
    return True

def LonhonmaSV(msv):
    while True:
        if ktnt(msv):
            return msv
        msv += 1

def NhohonmaSV(msv):
    while True:
        if ktnt(msv):
            return msv
        msv -= 1

def sntganmaSV(msv):
    solon = LonhonmaSV(msv)
    sonho = NhohonmaSV(msv)
    if msv - sonho > solon - msv:
        return solon
    else: 
        return sonho

def nhanbinhphuongcolap(a, k, n):
    ds_k = []
    while k > 0:
        r = k % 2
        ds_k.append(r)
        k = int(k // 2)
    A = a
    if ds_k[0] == 1:
        b = a
    else:
        b = 1
    for i in range(1, len(ds_k)):
        A = (A*A) % n 
        if ds_k[i] == 1:
            b = (A*b) % n
    return b

while True:
    try:
        a = int(input("Nhap SBD: "))
        if a<= 0:
            raise ValueError("Nhap lai SBD")
        break
    except ValueError as p:
        print(p)
msv = 190522
k = sntganmaSV(msv)
n = 123456
print(nhanbinhphuongcolap(a, k, n))

    