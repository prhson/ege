from turtle import *

screensize(10_000, 10_000)
tracer(0)
lt(90)
m = 10

for i in range(3):
    fd(27 * m)
    rt(90)
    fd(12 * m)
    rt(90)

up()
fd(4 * m)
rt(90)
bk(6 * m)
lt(90)
down()

for i in range(4):
    fd(83 * m)
    rt(90)
    fd(77 * m)
    rt(90)

for x in range(-59, 19):
    for y in range(-60, 24):
        teleport(x * m, y * m)
        dot(3, 'red')

print()
update()
done()