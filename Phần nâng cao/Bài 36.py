def loai_bo_trung_lap(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

def last_occrurrence_each_char(text1, text2):
    last_occurrence = {}
    for i in range(len(text1)):
        last_occurrence[text1[i]] = i
    ds = loai_bo_trung_lap(text2)
    for i in range(len(ds)):
        if ds[i] not in last_occurrence:
            last_occurrence[ds[i]] = -1
    return last_occurrence

def boyer_moore(T, P):
    L = last_occrurrence_each_char(P,T)
    m = len(T)
    n = len(P)
    i = n - 1 
    j = n - 1
    while i < m:
        if T[i] == P[j]:
            if j == 0:
                return i 
            else:
                i = i - 1 
                j = j - 1
        else:
            l = L[T[i]]
            i = i + n - min(j, 1 + l)
            j = n - 1
    if i > m - 1:
        return -1
    
if __name__ == '__main__':
    T = input("Nhap doan van ban T:")
    P = input("Nhap doan van ban P: ")
    result = boyer_moore(T, P)
    if result != 1:
        print("P trung voi chuoi ki tu con trong T tai vi tri", result)
    else:
        print("Khong trung khop")



