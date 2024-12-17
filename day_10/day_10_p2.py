with open("./day_10/day_10.txt") as fin:
    lines = fin.read().strip().split()

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
road_map = {}
queue = []
for r, line in enumerate(lines):
    for c, item in enumerate(line):
        road_map[(r, c)] = int(item)
        if int(item) == 0:
            queue.append((r, c))

ans = 0
for q in queue:
    route = [q]
    comp_routes = 0
    for r, c in route:
        val = road_map[(r, c)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if (nr, nc) in road_map and road_map[(nr, nc)] == val + 1:
                route.append((nr, nc))
                if val + 1 == 9:
                    comp_routes += 1
    ans += comp_routes

print(ans)


