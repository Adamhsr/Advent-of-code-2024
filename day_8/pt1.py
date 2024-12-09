with open('./day_8/input.txt', 'r') as file:
    inp = file.read().splitlines()

filled = set()

lx = len(inp)
ly = len(inp[0])

letterPos = {}

for x in range(len(inp)):
    for y in range(len(inp[0])):
        if inp[x][y] == '.':
            continue
        letter = inp[x][y]
        filled.add((x, y))
        if letter in letterPos:
            letterPos[letter].append((x, y))
        else:
            letterPos[letter] = [(x, y)]

antennas = set()
c = 0

for key in letterPos:
    letters = letterPos.get(key)
    for i in range(len(letters)):
        for j in range(len(letters)):
            x1, y1 = letters[i]
            x2, y2 = letters[j]
            nx = 2 * x1 - x2
            ny = 2 * y1 - y2
            if nx < 0 or ny < 0 or nx >= lx or ny >= ly or (nx, ny) in letters:
                pass
            else:
                antennas.add((nx, ny))

print(len(antennas))
