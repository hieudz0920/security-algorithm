def tien_to(s):
    ds = []
    for i in range(len(s)+1):
        ds.append(s[:i])
    return ds

def hau_to(s):
    ds = []
    for i in range(len(s)):
        ds.append(s[i:])
        return ds
    
def so_sanh(s):
    ds1 = tien_to(s)
    ds2 = hau_to(s)
    do_dai = []
    for i in range(len(ds1)):
        for j in range(len(ds2)):
            if ds2[j] == ds1[i]:
                do_dai.append(len(ds1[i]))
    if len(do_dai) == 0:
        return 0
    else: 
        maxdodai = max(do_dai)
        return maxdodai
    
def failure_function(P):
    ds = {}
    for j in range(len(P)):
        if j == 0:
            ds[j] = -1
        else:
            splitP = P[0:j]
            result = so_sanh(splitP)
            ds[j] = result
    return ds

def KMP(T, P):
    f = failure_function(P)
    m = len(T)
    n = len(P)
    i = 0
    j = 0
    while i <= m - n :
        while j < n and T[i + j] == P[j]:
            j += 1
        if j == n:
            return i
        if j == 0:
            i += 1
        else:
            i = i + j - f[j]
            j = f[j]
            if f[j] == -1:
                j = 0
    return -1 

def main():
    T = input("Nhap chuoi T: ")
    P = input("Nhap chuoi P: ")
    result = KMP(T, P)
    if result != -1:
        print(f"Mau {P} trung khop voi chuoi {T} tai vi tri {result}")
    else:
        print("Khong trung khop")

if __name__ == "__main__":
    main()

