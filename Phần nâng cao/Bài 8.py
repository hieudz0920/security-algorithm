def T_Prime(n):
    dem = 0
    for i in range(1, n+1):
        if n % i == 0:
            dem += 1
    if dem == 3:
            return True
    return False

while True:
    try:
        n = int(input("Nhap n: "))
        if n <= 0:
            raise ValueError("n la so nguyen duong, yeu cau nhap lai")
        break
    except ValueError as z:
        print(z)
a = []
for i in range(n +1):
    if T_Prime(i):
        a.append(i)
b = []
if a == b:
    print(f"Khong co so T-Prime nho hon {n}")
else:
    print(a)

