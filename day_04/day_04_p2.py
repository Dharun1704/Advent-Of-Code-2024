with open("./day_04/day_04.txt") as fin:
    lines = fin.read().split()

dirs = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
ans = 0

rows, cols = len(lines), len(lines[0])

for i in range(rows):
    for j in range(cols):
        if lines[i][j] == 'A':
            diags = [(i + dx, j + dy) for dx, dy in dirs]
            if all(0 <= x < rows and 0 <= y < cols for x, y in diags):
                chars = [lines[x][y] for x, y in diags]
                if chars.count('M') == 2 and chars.count('S') == 2 and chars[0] != chars[1]:
                    ans += 1

print(ans)


