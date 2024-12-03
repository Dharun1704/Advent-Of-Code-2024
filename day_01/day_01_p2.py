import math

with open('./day_01/day_01.txt', 'r') as fin:
    lines = fin.readlines()

a = []
b = []
for line in lines:
    p = line.strip().split(" ")
    a.append(p[0])
    b.append(p[-1])

s = 0
for i in range(0, len(a)):
    s += (int(a[i]) * b.count(a[i]))

print(s)
