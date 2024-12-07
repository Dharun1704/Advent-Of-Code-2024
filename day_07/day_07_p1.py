from itertools import product

with open("./day_07/day_07.txt") as fin:
    lines = fin.readlines()

def backtrack(idx, cur_res):
    if idx == len(numbers):
        if cur_res == target:
            res.append(cur_res)
        return
    backtrack(idx + 1, cur_res + numbers[idx])
    backtrack(idx + 1, cur_res * numbers[idx])

ans = 0
for line in lines:
    target, numbers = line.split(':')
    target = int(target)
    numbers = list(map(int, numbers.strip().split(' ')))
    n = len(numbers)
    found = False
    print(target, numbers)
    res = []
    backtrack(1, numbers[0])
    if res:
        ans += res[0]

print(ans)        
    

