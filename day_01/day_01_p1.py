import math

with open('./day_01/day_01.txt', 'r') as fin:
    lines = fin.readlines()

a = []
b = []
for line in lines:
    p = line.strip().split(" ")
    a.append(p[0])
    b.append(p[-1])

a.sort()
b.sort()
s = 0
for i in range(0, len(a)):
    x = int(a[i])
    y = int(b[i])
    if x >= y:
        s += x - y
    else:
        s += y - x

print(s)
