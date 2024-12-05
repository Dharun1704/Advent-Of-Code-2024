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
    inc_order = False
    
    for _ in range(len(update)):
        for i, val in enumerate(update):
            if val in rules_map:
                for j in range(i - 1, -1, -1):
                    if update[j] in rules_map[val]:
                        update[j], update[i] = update[i], update[j]
                        inc_order = True
                        break
    
    if inc_order:
        ans += update[len(update) // 2]

print(ans)
