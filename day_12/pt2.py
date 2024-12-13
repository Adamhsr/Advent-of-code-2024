with open("./day_12/input.txt", "r") as f:
    inp = list(map(list, f.read().splitlines()))


def side_finder(plots, lx, ly):
    sides = 0
    on_side0 = False
    for x in range(lx + 1):
        for y in range(ly + 1):
            if on_side0:
                on_side0 = (x, y) in plots and (x - 1, y) not in plots
            else:
                if (x, y) in plots and (x - 1, y) not in plots:
                    on_side0 = True
                    sides += 1

    on_side1 = False
    for x in range(lx + 1):
        for y in range(ly + 1):
            if on_side1:
                on_side1 = (x, y) not in plots and (x - 1, y) in plots
            else:
                if (x, y) not in plots and (x - 1, y) in plots:
                    on_side1 = True
                    sides += 1
    
    on_side0 = False
    for y in range(ly + 1):
        for x in range(lx + 1):
            if on_side0:
                on_side0 = (x, y) in plots and (x, y - 1) not in plots
            else:
                if (x, y) in plots and (x, y - 1) not in plots:
                    on_side0 = True
                    sides += 1

    on_side1 = False
    for y in range(ly + 1):
        for x in range(lx + 1):
            if on_side1:
                on_side1 = (x, y) not in plots and (x, y - 1) in plots
            else:
                if (x, y) not in plots and (x, y - 1) in plots:
                    on_side1 = True
                    sides += 1
    return sides


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
                if nx < 0 or ny < 0 or nx >= lx or ny >= ly or inp[nx][ny] != plant:
                    continue
                else:
                    searching.append((nx, ny))
        
        searched = searched.union(my_searched)
        print(area, side_finder(my_searched, lx, ly))
        total += area * side_finder(my_searched, lx, ly)

print(total)