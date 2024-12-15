
with open("./day_15/input.txt", "r") as f:
    inp = f.read().split("\n\n")

small_room = list( map( list, inp[0].split("\n")))
dirs = inp[1]

room = []
for level in inp[0].split("\n"):
    lane = []
    for thing in level:
        if thing == "#":
            lane = lane + ["#", "#"]
        if thing == ".":
            lane = lane + [".", "."]
        if thing == "O":
            lane = lane + ["[", "]"]
        if thing == "@":
            lane = lane + ["@", "."]
    room.append(lane)

from time import sleep

def try_push(x, y, dx, dy):
    obj = room[x][y]

    # sleep(0.2)
    # dis()
    # print(x, y, dx, dy, obj)
    if obj == "#":
        return False
    if obj == "]":
        return try_push(x, y - 1, dx, dy)
    if obj == ".":
        return True
    
    nx = x + dx
    ny = y + dy
    px = x - dx
    py = y - dy

    if obj == "@" and try_push(nx, ny, dx, dy):
        return True

    # were at a box
    if (dx, dy) == (0, -1):
        if try_push(nx, ny, dx, dy):
            return True
        return False
    if (dx, dy) == (0, 1):
        if try_push(nx + dx, ny + dy, dx, dy):
            return True
        return False
    
    # pushing up or down
    if try_push(nx, ny, dx, dy) and try_push(nx, ny + 1, dx, dy):
        return True
    return False

def push(x, y, dx, dy):
    obj = room[x][y]

    # sleep(0.2)
    # dis()
    # print(x, y, dx, dy, obj)
    if obj == "#":
        return False
    if obj == "]":
        return push(x, y - 1, dx, dy)
    if obj == ".":
        return True
    
    nx = x + dx
    ny = y + dy
    px = x - dx
    py = y - dy

    if obj == "@" and push(nx, ny, dx, dy):
        room[nx][ny] = "@"
        room[x][y] = "."
        return True

    # were at a box
    if (dx, dy) == (0, -1):
        if push(nx, ny, dx, dy):
            print("push left")
            room[nx][ny] = "["
            room[x][y] = "]"
            room[px][py] = "."
            return True
        return False
    if (dx, dy) == (0, 1):
        if push(nx + dx, ny + dy, dx, dy):
            room[nx + dx][ny + dy] = "]"
            room[nx][ny] = "["
            room[x][y] = "."
            return True
        return False
    
    # pushing up or down
    if push(nx, ny, dx, dy) and push(nx, ny + 1, dx, dy):
        room[nx][ny] = "["
        room[nx][ny + 1] = "]"
        room[x][y] = "."
        room[x][y+1] = "."
        return True
    return False

def dis():
    for x in range(len(room)):
        for y in range(len(room[0])):
            print(room[x][y], end="")
        print()

cx = None
cy = None

for x in range(len(room)):
        for y in range(len(room[0])):
            if room[x][y] == "@":
                cx = x
                cy = y

move_dict = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

for move in dirs:
    if move == "\n":
        continue
    
    dx, dy = move_dict[move]
    if try_push(cx, cy, dx, dy):
        push(cx, cy, dx, dy)
        cx += dx
        cy += dy

count = 0

for x in range(len(room)):
        for y in range(len(room[0])):
            if room[x][y] == "[":
                count += x * 100 + y

dis()
print(count)