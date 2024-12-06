with open('./day_6/input.txt', 'r') as file:
    inp = file.read().splitlines()

from time import sleep

result = 0

obstacles = set()
visited = set()

guard = []
dir = [-1, 0]

for i in range(len(inp)):
    for j in range((len(inp[0]))):
        if inp[i][j] == "#":
            obstacles.add(str(i) + "," + str(j))
        elif inp[i][j] == "^":
            guard = [i, j]

def xyin(x, y):
    return str(x) + "," + str(y) in obstacles

while 0 <= guard[0] < len(inp) and 0 <= guard[1] < len(inp[0]):
    visited.add(str(guard[0]) + "," + str(guard[1]))
    if xyin(guard[0] + dir[0], guard[1] + dir[1]):
        if dir == [-1, 0]:
            dir = [0, 1]
        elif dir == [0, 1]:
            dir = [1, 0]
        elif dir == [1, 0]:
            dir = [0, -1]
        elif dir == [0, -1]:
            dir = [-1, 0]
    else:
        guard[0] = guard[0] + dir[0]
        guard[1] = guard[1] + dir[1]

print(len(visited))