with open("./day_09/day_09.txt") as fin:
    line = fin.read().strip()

disk_arr = [i // 2 if i % 2 == 0 else '.' for i, item in enumerate(line) for _ in range(int(item))]

start, end = 0, len(disk_arr) - 1
while start < end:
    while start < len(disk_arr) and disk_arr[start] != '.':
        start += 1
    while disk_arr[end] == '.':
        end -= 1
    temp = disk_arr[end]
    if start > end:
        break
    disk_arr[start], disk_arr[end] = disk_arr[end], '.'

ans = sum(i * item for i, item in enumerate(disk_arr) if item != '.')
print(ans)