with open('./day_9/input.txt', 'r') as file:
    inp = list(file.read())

result = 0
pos = 0

space = []

for i, n in enumerate(inp):
    if i % 2 == 1:
        space.append((-1, int(n)))
    else:
        space.append((int(i/2), int(n)))

new = space[::]

for i in reversed(range(len(space))):
    if space[i][0] == -1:
        continue
    id = space[i][0]
    length = space[i][1]
    moved = False
    for j in range(len(new)):
        if new[j][0] == id:
            break
        if new[j][0] == -1 and length <= new[j][1]:
            moved = True
            if length == new[j][1]:
                new[j] = space[i]
                break
            new[j] = [space[i], (-1, new[j][1] - length)]
            break
    
    nnew = []
    for l in new:
        if type(l) == list:
            nnew.append(l[0])
            nnew.append(l[1])
        else:
            nnew.append(l)

    if moved:

        new = []
        first = True
        for blkk in nnew:
            if blkk[0] == id and first:
                new.append(blkk)
                first = False
            elif blkk[0] == id:
                new.append((-1, blkk[1]))
            else:
                new.append(blkk)


thingy = []
for t in new:
    thingy += [t[0]] * t[1]

for i, n in enumerate(thingy):
    if n == -1:
        continue
    result += i * n



print(result)
