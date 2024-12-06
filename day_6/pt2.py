with open('./day_6/input.txt', 'r') as file:
    inp = file.read().splitlines()

result = 0

obstacles = set()
visited = set()

guardog = []
dirog = [-1, 0]
dir = [-1, 0]


for i in range(len(inp)):
    for j in range((len(inp[0]))):
        if inp[i][j] == "#":
            obstacles.add((i, j))
        elif inp[i][j] == "^":
            guardog = [i, j]

guard = guardog[::]

def xyin(x, y, obs):
    return (x, y) in obs

while 0 <= guard[0] < len(inp) and 0 <= guard[1] < len(inp[0]):
    visited.add(tuple(guard))
    if xyin(guard[0] + dir[0], guard[1] + dir[1], obstacles):
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

def loop(_obs, _grd, _d):
    obs = _obs.copy()
    grd = _grd.copy()
    d = _d.copy()
    vst = set()
    while 0 <= grd[0] < len(inp) and 0 <= grd[1] < len(inp[0]):
        vst.add((grd[0], grd[1], d[0], d[1]))
        if xyin(grd[0] + d[0], grd[1] + d[1], obs):
            if d == [-1, 0]:
                d = [0, 1]
            elif d == [0, 1]:
                d = [1, 0]
            elif d == [1, 0]:
                d = [0, -1]
            elif d == [0, -1]:
                d = [-1, 0]
        else:
            grd[0] += d[0]
            grd[1] += d[1]
        
        if (grd[0], grd[1], d[0], d[1]) in vst:
            return True
    return False


for n, p in enumerate(visited):
    if p == tuple(guardog):
        continue
    a = obstacles.copy()
    a.add(p)
    if loop(a, guardog[::], [-1, 0]):
        result += 1

print(result)