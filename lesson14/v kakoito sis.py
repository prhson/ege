def f(n):
    a=[]
    while n>0:
        a.append(n % 49)
        n //= 49
    return a[::1]

n49 = f(2*2401**525+3+343**524-4*49**8)
cnt=0
for d in n49:
    if d <=9:
        cnt+=1
print(cnt)
