from string import printable as alph

for x in alph[:24]:
    num_1 = int(f'A4{x}7F2', 25)
    num_2 = int(f'N{x}G5{x}H', 25)
    num_3 = int(f'74{x}M26',25)
    num = num_1 + num_2 + num_3
    if num % 24 == 0:
        print(num // 24)
