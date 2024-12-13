with open("./day_12/input.txt", "r") as f:
    inp = list(map(list, f.read().splitlines()))

total = 0
searched = set()

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

lx = len(inp)
ly = len(inp[0])

for i in range(lx):
    for j in range(ly):
        plant = inp[i][j]
        if (i, j) in searched:
            continue

        searching = [(i, j)]
        area = 0
        perimiter = 0
        my_searched = set()

        while searching:
            x, y = searching.pop()
            if (x, y) in my_searched:
                continue
            my_searched.add((x, y))
            area += 1

            for dx, dy in dirs:
                nx = x + dx
                ny = y + dy
                if (nx, ny) in my_searched:
                    continue
                if nx < 0 or ny < 0 or nx >= lx or ny >= ly:
                    perimiter += 1
                    continue
                if inp[nx][ny] == plant:
                    searching.append((nx, ny))
                else:
                    perimiter += 1
                    continue
        
        searched = searched.union(my_searched)
        total += area * perimiter

print(total)