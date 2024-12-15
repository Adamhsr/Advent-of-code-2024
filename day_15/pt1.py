with open("./day_15/input.txt", "r") as f:
    inp = f.read().split("\n\n")

room = list( map( list, inp[0].split("\n")))
dirs = inp[1]

def try_push(x, y, dx, dy):
    if room[x][y] == "#":
        return False


    nx = x + dx
    ny = y + dy
    if room[nx][ny] == '.' or try_push(nx, ny, dx, dy):
        room[nx][ny] = room[x][y]
        room[x][y] = '.'
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
        cx += dx
        cy += dy

count = 0

for x in range(len(room)):
        for y in range(len(room[0])):
            if room[x][y] == "O":
                count += x * 100 + y

print(count)