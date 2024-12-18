with open("./day_12/day_12.txt") as fin:
    grid = fin.read().strip().split()
m, n = len(grid), len(grid[0])

def get_region_and_cost(dr, dc):
    plant, visited = grid[dr][dc], set()
    fence, queue = 0, [(dr, dc)]
    while queue:
        r, c = queue.pop()
        if (r, c) in visited:
            continue
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != plant:
            fence += 1
            continue
        visited.add((r, c))
        queue.extend([(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)])
    return visited, len(visited) * fence

total_cost, visited = 0, set()
for r in range(m):
    for c in range(n):
        if (r, c) not in visited:
            region, cost = get_region_and_cost(r, c)
            visited.update(region)
            total_cost += cost

print(total_cost)