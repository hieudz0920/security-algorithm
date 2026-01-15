import math
p = 2147483647
w = 8

def mang(a, w, p):
    result = []
    m = round(math.log2(p))
    t = round(m/w)
    n = [pow(2, i * w) for i in range(t)]
    for i in n[::-1]:
        result.append(math.floor(a/i))
        a = a % i
    return result

while True:
    try:
        a = int(input("Nhap so nguyen A: "))
        b = int(input("Nhap so nguyen B: "))
        if a <=0 or b <= 0 :
            raise ValueError("Nhap lai ")
        break
        
    except ValueError as z:
        print(z)

c = a + b
mang_c = mang(c, w, p)
print("Dang so nguyen la: ", c)
print("Dang mang la: ", mang_c)