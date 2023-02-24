def digital_root(n):
    numarr = [int(i) for i in str(n)]
    a = 0
    for num in numarr:
        a = a+num
    if a >= 10:
        b = digital_root(a)
    else:
        return a
    return b
        
print(digital_root(15)) # 6
print(digital_root(942)) # 6
print(digital_root(132189)) # 6
print(digital_root(493193)) # 2
print(digital_root(30142200412699912))