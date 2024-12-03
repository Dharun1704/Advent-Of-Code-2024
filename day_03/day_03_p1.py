import re

with open("./day_03/day_03.txt") as fin:
    lines = fin.read().replace('\n', ' ')

pattern1 = r"mul\(\d{1,3},\d{1,3}\)"
ops = re.findall(pattern1, lines)
ans = sum(int(a) * int(b) for a, b in [re.findall(r"\d+", op) for op in ops])

print(ans)
