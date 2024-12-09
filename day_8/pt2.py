with open('./day_8/input.txt', 'r') as file:
    inp = file.read().splitlines()

filled = set()

lx = len(inp)
ly = len(inp[0])

letterPos = {}

for x in range(len(inp)):
    for y in range(len(inp[0])):
        if inp[x][y] == '.' or inp[x][y] == '#':
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
        for j in range(i + 1, len(letters)):
            x1, y1 = letters[i]
            x2, y2 = letters[j]
            dx = x1 - x2
            dy = y1 - y2
            nx = x1
            ny = y1
            
            while nx >= 0 and ny >= 0 and nx < lx and ny < ly:
                antennas.add((nx, ny))
                nx = nx - dx
                ny = ny - dy
                
            nx = x1 + dx
            ny = y1 + dy
            while nx >= 0 and ny >= 0 and nx < lx and ny < ly:
                antennas.add((nx, ny))
                nx = nx + dx
                ny = ny + dy

print(len(antennas))