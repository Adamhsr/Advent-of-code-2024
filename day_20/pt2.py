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


raceway = []
racecar = (startx, starty)

while True:
    x, y = racecar
    raceway.append((x, y))
    if inp[x][y] == "E":
        break
    for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if inp[nx][ny] != "#" and (nx, ny) not in raceway:
            racecar = (nx, ny)
            break

total = 0

for i in range(len(raceway)):
    x, y = raceway[i]
    for j in range(len(raceway[i+100:])):
        tx, ty = raceway[i+j+100]
        cheattime = abs(tx - x) + abs(ty - y)
        saved = j + 101 - cheattime
        if cheattime <= 20 and saved >= 100:
            total += 1


print(total)