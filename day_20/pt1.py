with open('./day_20/input.txt', 'r') as file:
    inp = file.read().split("\n")

startx = starty = endx = endy = 0

for x in range(len(inp)):
    for y in range(len(inp[0])):
        if inp[x][y] == "S":
            startx = x
            starty = y
        elif inp[x][y] == "E":
            endx = x
            endy = y


distance = {}
racecar = (endx, endy, 0)

while True:
    x, y, d = racecar
    distance[(x, y)] = d
    if inp[x][y] == "S":
        break
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if inp[nx][ny] != "#" and (nx, ny) not in distance:
            racecar = (nx, ny, d + 1)
            break

total = 0

for (x, y), d in distance.items():
    for dx, dy in [(-2, 0), (0, -2), (2, 0), (0, 2)]:
        nx = x + dx
        ny = y + dy
        if (nx, ny) in distance and d - 2 - distance[(nx, ny)] >= 100:
            total += 1

print(total)