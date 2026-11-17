ans= []
for x in range(1,3001):
    num = 9**150+9**30-x
    cnt = 0
    while num:
        if num % 3 == 0: cnt += 1
        num //= 3
    if cnt == 1:
        ans.append(x)
print(max(ans)