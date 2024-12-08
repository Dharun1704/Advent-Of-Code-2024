from collections import defaultdict
from itertools import combinations, count

with open("./day_08/day_08.txt") as fin:
    lines = fin.read().strip()

grid = [list(row) for row in lines.split("\n")]
rows, cols = len(grid), len(grid[0])

def find_antinodes(ant1, ant2):
    r1, c1 = ant1
    r2, c2 = ant2
    r = 2 * r2 - r1
    c = 2 * c2 - c1
    if 0 <= r < rows and 0 <= c < cols:
        yield r, c

freqs = defaultdict(set)
antinodes = set()

for r, row in enumerate(grid):
	for c, cell in enumerate(row):
		if cell != '.':
			freqs[cell].add((r, c))

for ant in freqs.values():
	for a, b in combinations(ant, 2):
		antinodes.update(find_antinodes(a, b))
		antinodes.update(find_antinodes(b, a))

print(f'Part 1 solution : {len(antinodes)}')
