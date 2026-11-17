for p in range(16, 60):
    n1 = int('17496', p)
    n2 = int('91F83', p)
    n3 = int('D9543', p)
    n = n1 + n2 + n3
    if n % 12 == 0:
        print(n // 12)
        break