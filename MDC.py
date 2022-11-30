def mdc(a,b):
    for i in range(1,a):
        if a % i == 0 and b % i == 0:
            d = i
    return d        

print(mdc(22,120))








