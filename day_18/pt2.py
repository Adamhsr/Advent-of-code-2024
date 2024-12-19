with open('./day_18/input.txt', 'r') as file:
    inp = file.read().split("\n")

lx = ly = 70

def cant_solve(corrupted):
    locations = set([(0, 0)])
    visited = set()
    while (lx, ly) not in locations:
        if not locations:
            return True
        
        visited = visited.union(locations)
        new_locations = set()
        for x, y in locations:
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= lx and 0 <= ny <= ly and (nx, ny) not in corrupted and (nx, ny) not in visited:
                    new_locations.add((nx, ny))
        locations = new_locations
    return False


corrupted = set()

for i in range(len(inp)):
    x, y = inp[i].split(",")
    corrupted.add((int(x), int(y)))
    
    if cant_solve(corrupted):
        print(str(x) + "," + str(y))
        exit()