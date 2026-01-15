def Q_prime(n):
    dem = 0
    for i in range(1, n+1):
        if n % i == 0:
            dem += 1
    if dem == 4:
        return True
    return False


n = int(input("Nhap n: "))
if n < 0:
    n = n * (-1)
        

a = []
for i in range(n + 1):
    if Q_prime(i):
        a.append(i)
empty_list = []
if a == empty_list:
    print(f"Khong co so Q-Prime nao nho hon hoac bang {n}")
else:
    print(f"Cac so Q-Prime nho hon hoac bang {n} la: {a}")

            