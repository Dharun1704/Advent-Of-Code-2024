from collections import defaultdict

with open("./day_11/day_11.txt") as fin:
    stones = list(map(int, fin.read().strip().split()))

counter = {stone: 1 for stone in stones}
print(counter)
k = 75

for i in range(k):
    res = defaultdict(int) 
    for item, val in counter.items():
        if item == 0:
            res[1] += val
        elif (length := len(str(item))) % 2 == 0:
            half = length // 2
            res[int(str(item)[:half])] += val
            res[int(str(item)[half:])] += val
        else:
            res[item * 2024] += val
    counter = res
    if i in {24, 74}:
        print(sum(counter.values()))