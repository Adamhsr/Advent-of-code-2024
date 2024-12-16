with open("./day_16/input.txt", "r") as f:
    inp = list(map(list, f.read().split("\n")))

sx = xy = 0
gx = gy = 0

for x in range(len(inp)):
    for y in range(len(inp[0])):
        if inp[x][y] == "S":
            sx = x
            sy = y
        if inp[x][y] == "E":
            gx = x
            gy = y

from collections import deque

visited = {}
scores = {}
good_paths = []

togo = deque([(sx, sy, 0, 1, 0, [(sx, sy)])])

min_score = -1

while togo:
    x, y, dx, dy, score, path = togo.popleft()
    if (x, y) in scores and score > scores[(x, y)]:
        pass
    else:
        scores[(x, y)] = score
    

    if (x, y, dx, dy) in visited and visited[(x, y, dx, dy)] <= score:
        continue

    visited[(x, y, dx, dy)] = score

    if inp[x][y] == "E" and (score < min_score or min_score == -1):
        if min_score == score:
            good_paths.append(path)
        else:
            good_paths = [path]
        
        min_score = score

    nx = x + dx
    ny = y + dy
    if inp[nx][ny] != "#":
        togo.append((nx, ny, dx, dy, score + 1, path + [(nx, ny)]))
    togo.append((x, y, dy, -dx, score + 1000, path))
    togo.append((x, y, -dy, dx, score + 1000, path))


spots = set()

backwards = deque([(gx, gy, 0, 1), (gx, gy, 0, -1), (gx, gy, 1, 0), (gx, gy, -1, 0)])

while backwards:
    x, y, dx, dy = backwards.pop()
    spots.add((x, y))

    if scores[(x, y)] == 0:
        continue

    possibilities = [(x, y, 0, 1), (x, y, 0, -1), (x, y, 1, 0), (x, y, -1, 0),
                     (x - dx, y - dy, dx, dy)]
    for nxt in possibilities:
        if nxt in visited:
            if visited[nxt] < visited[(x, y, dx, dy)]:
                backwards.append(nxt)

# for x in range(len(inp)):
#     for y in range(len(inp[0])):
#         if inp[x][y] == ".":
#             print(scores[(x, y)] // 1000, end="")
#         else:
#             print(inp[x][y], end="")
#     print()

# for x in range(len(inp)):
#     for y in range(len(inp[0])):
#         if (x, y) in spots:
#             print("O", end="")
#         else:
#             print(inp[x][y], end="")
#     print()

print(min_score, len(spots))