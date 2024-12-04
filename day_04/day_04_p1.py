with open("./day_04/day_04.txt") as fin:
    lines = fin.read().split()

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]

def search_xmas(x, y, dx, dy, word):
    for i in range(len(word)):
        a, b = x + i * dx, y + i * dy
        if not(0 <= a < rows and 0 <= b < cols) or lines[a][b] != word[i]:
            return False
    return True

rows, cols = len(lines), len(lines[0])
occurs_cnt = 0
word = "XMAS"

for x in range(rows):
    for y in range(cols):
        for dx, dy in dirs:
            if search_xmas(x, y, dx, dy, word):
                occurs_cnt += 1

print(occurs_cnt)
