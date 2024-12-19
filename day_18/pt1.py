with open('./day_18/input.txt', 'r') as file:
    inp = file.read().split("\n")[0:1024]

corrupted = set()
for loc in inp:
    x, y = loc.split(",")
    corrupted.add((int(x), int(y)))

locations = set([(0, 0)])
visited = set()

lx = ly = 70


# flood fill search
steps = 0
while (lx, ly) not in locations:
    steps += 1

    visited = visited.union(locations)
    new_locations = set()
    for x, y in locations:
        for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= lx and 0 <= ny <= ly and (nx, ny) not in corrupted and (nx, ny) not in visited:
                new_locations.add((nx, ny))
    locations = new_locations


print(steps)