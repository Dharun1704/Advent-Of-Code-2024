with open("./day_09/day_09.txt") as fin:
    line = fin.read().strip()

disk_arr = []
for i, item in enumerate(line):
    for j in range(int(item)):
        if i % 2 == 1:
            disk_arr.append('.')
        else:
            disk_arr.append(i // 2)

start = 0
end = len(disk_arr) - 1
while start < len(disk_arr):
    temp = 0
    while start < len(disk_arr) and disk_arr[start] != '.':
        start += 1
    while disk_arr[end] == '.':
        end -= 1
    temp = disk_arr[end]
    if start > end:
        break
    disk_arr[end] = '.'
    disk_arr[start] = temp

ans = 0
for i, item in enumerate(disk_arr):
    if item != '.':
        ans += i * item
    if item == '.':
        break

print(ans)
