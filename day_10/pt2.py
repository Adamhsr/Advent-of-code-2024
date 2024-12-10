with open('./day_10/input.txt', 'r') as file:
    inp = file.read().split("\n")

trailheads = []

for x, line in enumerate(inp):
    for y, chat in enumerate(line):
        if chat == "0":
            trailheads.append((x, y))


total = 0

for trail in trailheads[::]:
    paths = [trail]
    while paths:
        x, y = paths.pop()
        height = int(inp[x][y])
        if height == 9:
            total += 1
            continue
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if nx >= 0 and ny >= 0 and nx < len(inp) and ny < len(inp[0]) and int(inp[nx][ny]) == 1 + height:
                paths.append((nx, ny))

print(total)