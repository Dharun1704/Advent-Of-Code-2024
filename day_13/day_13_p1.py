from sympy import symbols, Eq, solve, simplify

with open("./day_13/day_13.txt") as fin:
    slots = fin.read().strip().split('\n\n')

total = 0

for slot in slots:
    instruct = slot.split('\n')
    x, y = symbols('x,y')
    x_axis, y_axis = [], []
    for item in instruct:
        if item.split()[0] == 'Button':
            a = int(item.split(':')[1].split(',')[0].split('+')[1])
            b = int(item.split(':')[1].split(',')[1].split('+')[1])
            x_axis.append(a)
            y_axis.append(b)
        elif item.split(':')[0] == 'Prize':
            c1 = int(item.split(':')[1].split(',')[0].split('=')[1])
            c2 = int(item.split(':')[1].split(',')[1].split('=')[1])
            x_axis.append(c1)
            y_axis.append(c2)
    eq_1 = Eq((x_axis[0] * x + x_axis[1] * y), x_axis[2])
    eq_2 = Eq((y_axis[0] * x + y_axis[1] * y), y_axis[2])
    ans = solve((eq_1, eq_2), (x, y))
    if (simplify(ans[x]).is_integer and 
        simplify(ans[y]).is_integer and 
        ans[x] <= 100 and ans[y] <= 100):
        total += (ans[x] * 3) + (ans[y] * 1)

print(total)