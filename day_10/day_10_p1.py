with open("./day_10/day_10.txt") as fin:
    lines = fin.read().strip().split()

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
road_map = {(r, c): int(item) for r, line in enumerate(lines) for c, item in enumerate(line)}
queue = [(r, c) for (r, c), val in road_map.items() if val == 0]

ans = 0
for q in queue:
    route, comp_routes = [q], 0
    for r, c in route:
        val = road_map[(r, c)]
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if road_map.get((nr, nc)) == val + 1 and (nr, nc) not in route:
                route.append((nr, nc))
                if val + 1 == 9:
                    comp_routes += 1
    ans += comp_routes

print(ans)


