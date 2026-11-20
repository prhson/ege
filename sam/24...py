from turtle import *

screensize(10_000, 10_000)
tracer(0)
lt(90)
m = 15

for i in range(2):
    fd(3 * m)
    rt(90)
    fd(20 * m)
    rt(90)

up()
bk(8 * m)
rt(90)
fd(9 * m)
lt(90)
down()

for i in range(2):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)

for x in range(9, 18):
    for y in range(0, 4):
        teleport(x * m, y * m)
        dot(3, 'red')

print()
update()
done()
print (18-9)*(4-0)