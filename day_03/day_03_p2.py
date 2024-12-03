import re

with open("./day_03/day_03.txt") as fin:
    lines = fin.read().replace('\n', ' ')

mul_ptrn = r"mul\(\d{1,3},\d{1,3}\)"
skip_ptrn = r"don't\(\)(.*?)(do\(\)|$)"

skips = re.sub(skip_ptrn, '', lines)
ops = re.findall(mul_ptrn, skips)

ans = sum(int(a) * int(b) for a, b in [re.findall(r"\d+", op) for op in ops])

print(ans)
