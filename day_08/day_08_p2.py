from collections import defaultdict
from itertools import combinations, count

with open("./day_08/day_08.txt") as fin:
    lines = fin.read().strip()

grid = [list(row) for row in lines.split("\n")]
rows, cols = len(grid), len(grid[0])

def find_line(ant1, ant2):
	r1, c1 = ant1
	r2, c2 = ant2
	d_row = r2 - r1
	d_col = c2 - c1
	for item in count(0):
		r = r1 + item * d_row
		c = c1 + item * d_col
		if 0 <= r < rows and 0 <= c < cols:
			yield r, c
		else:
			break

freqs = defaultdict(set)
line_points = set()

for r, row in enumerate(grid):
	for c, cell in enumerate(row):
		if cell != '.':
			freqs[cell].add((r, c))

for ant in freqs.values():
	for a, b in combinations(ant, 2):
		line_points.update(find_line(a, b))
		line_points.update(find_line(b, a))

print(f'Part 2 solution : {len(line_points)}')
