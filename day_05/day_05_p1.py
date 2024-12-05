from collections import defaultdict

with open("./day_05/day_05.txt") as fin:
    rules, updates = fin.read().split('\n\n')

rules_map = defaultdict(list)
for rule in rules.split():
    key, value = map(int, rule.split('|'))
    rules_map[key].append(value)

ans = 0
for update in updates.split():
    update = list(map(int, update.split(',')))
    skip = False
    for i, val in enumerate(update):
        if not skip and val in rules_map.keys():
            values = rules_map[val]
            for j in range(i - 1, -1, -1):
                if update[j] in values:
                    skip = True
                    break
    if not skip:
        ans += update[int(len(update) / 2)]

print(ans)
