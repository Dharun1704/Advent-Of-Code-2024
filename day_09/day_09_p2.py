with open("./day_09/day_09.txt") as fin:
    line = fin.read().strip()

idx = 0
disk_map = {}
keys = []
emptys = []
for i,item in enumerate(line):
    f = idx * i
    if i % 2 == 0: 
        keys.append(i)
        disk_map[i] = int(item) * [i // 2]
    else:
        emptys.append(i)
        disk_map[i] = int(item)*['.']
    idx += 1

for k in keys[::-1]:
    disk = len(disk_map[k])
    temp = []
    for i in emptys:
        if i > k:
            break
        item_count = disk_map[i].count('.')
        if item_count == 0:
            temp.append(i)
        if disk <= item_count:
            idx = disk_map[i].index('.')
            disk_map[i] = disk_map[i][:idx] + disk_map[k] + (item_count - disk)*['.']
            disk_map[k] = disk * ['.']
            break

    for i in temp:
        emptys.remove(i)

disk = []
for i in disk_map:
    disk += disk_map[i]

ans = 0
for i, item in enumerate(disk):
    if item != '.':
        ans += i * item

print(ans)