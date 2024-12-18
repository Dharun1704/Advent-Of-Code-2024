# solved with help of reddit
# key points:
# 1. Repesenting the grid as complex number helps with basic dfs
# 2. Convert grid to complex numbers
# 3. Loop through all locations on the grid.
# 4. Get the area/region unless we already calculated this one
# 5. Calculate the perimeter by accumulating legal neighbors that aren't within the current region.
# 6. Calculate the sides by tracing outside perimeters clockwise, starting at the bottom leftmost point, and always
#    keeping the area to our right, and count the number of turns we take. We proceed similarly on the inside holes, except
#    we start at the bottom rightmost point in the perimeter section, and keep the area to our right the whole time.
#    Use complex numbers to keep track of direction of movement, and where the shape is (always to our right).
#    Keep removing points from border points left to process until no new sections of border are left. I could have
#    used only a direction of movement pointer, but having a "wall is to the right" complex number too is just easier.
#    Also rotations are calculated using complex multiplication.

with open("./day_12/day_12.txt") as fin:
    data = fin.read().splitlines()

grid_map = {i + j * 1j: val for i, row in enumerate(data) for j, val in enumerate(row)}

def dfs(cur_pos, plant, fence, region, dr=None):
    if cur_pos in viz and grid_map.get(cur_pos) == plant:
        return
    if grid_map.get(cur_pos) != plant:
        fence.add((cur_pos, dr))
        return
    viz.add(cur_pos)
    region.add(cur_pos)
    for dr in dirs:
        dfs(cur_pos + dr, plant, fence, region, dr)

    neighbors = {(p + dr * 1j, dr) for p, dr in fence}
    return len(region), len(fence), len(fence - neighbors)

dirs = (1, -1, 1j, -1j)
viz = set()
regions = [dfs(pos, plant, set(), set()) for pos, plant in grid_map.items() if pos not in viz]
ans = sum(area * sides for area, perim, sides in regions)
print(ans)
