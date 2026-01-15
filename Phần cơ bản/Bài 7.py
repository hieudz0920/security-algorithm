import math 
def reverse_number(n):
    str_number = str(n)
    reversed_str = str_number[::-1]
    reversed_num = int(reversed_str)
    return reversed_num

def ktnt(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)+1)):
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
a = []
for i in range(1, n):
    if ktnt(i) and ktnt(reverse_number(i)):
        a.append(i)

print(a)

    
    