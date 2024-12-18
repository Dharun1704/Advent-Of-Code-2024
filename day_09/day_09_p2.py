with open("./day_09/day_09.txt") as fin:
    line = fin.read().strip()

idx = 0
disk_map = {i: [i // 2] * int(item) if i % 2 == 0 else ['.'] * int(item) for i, item in enumerate(line)}
keys = [i for i in disk_map if i % 2 == 0]
emptys = [i for i in disk_map if i % 2 == 1]

for k in keys[::-1]:
    disk = len(disk_map[k])
    for i in emptys:
        if i > k:
            break
        empty_count = disk_map[i].count('.')
        if disk <= empty_count:
            idx = disk_map[i].index('.')
            disk_map[i][idx:idx + disk] = disk_map[k]
            disk_map[k] = disk * ['.']
            break

disk = [item for items in disk_map.values() for item in items]
ans = sum(i * item for i, item in enumerate(disk) if item != '.')
print(ans)