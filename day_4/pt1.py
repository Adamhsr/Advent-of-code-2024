with open('./day_4/input.txt', 'r') as file:
    inp = file.readlines()

sum = 0

for x in range(len(inp)):
    for y in range(len(inp[0])):
        # - forwards
        try:
            if inp[x][y] == "X" and inp[x][y+1] == "M" and inp[x][y+2] == "A" and inp[x][y+3] == "S":
                sum += 1
        except IndexError:
            x += 0

        # - backwards
        try:
            if inp[x][y] == "S" and inp[x][y+1] == "A" and inp[x][y+2] == "M" and inp[x][y+3] == "X":
                sum += 1
        except IndexError:
            x += 0
        
        # | forwards
        try:
            if inp[x][y] == "X" and inp[x+1][y] == "M" and inp[x+2][y] == "A" and inp[x+3][y] == "S":
                sum += 1
        except IndexError:
            x += 0

        # | backwards
        try:
            if inp[x][y] == "S" and inp[x+1][y] == "A" and inp[x+2][y] == "M" and inp[x+3][y] == "X":
                sum += 1
        except IndexError:
            x += 0
        
        # \ forwards
        try:
            if inp[x][y] == "X" and inp[x+1][y+1] == "M" and inp[x+2][y+2] == "A" and inp[x+3][y+3] == "S":
                sum += 1
        except IndexError:
            x += 0

        # \ backwards
        try:
            if inp[x][y] == "S" and inp[x+1][y+1] == "A" and inp[x+2][y+2] == "M" and inp[x+3][y+3] == "X":
                sum += 1
        except IndexError:
            x += 0

        # / forwards
        try:
            if (y - 3) > -1 and inp[x][y] == "X" and inp[x+1][y-1] == "M" and inp[x+2][y-2] == "A" and inp[x+3][y-3] == "S":
                sum += 1
        except IndexError:
            x += 0

        # / backwards
        try:
            if (y - 3) > -1 and (inp[x][y] == "S") and (inp[x+1][y-1] == "A") and (inp[x+2][y-2] == "M") and (inp[x+3][y-3] == "X"):
                sum += 1
        except IndexError:
            x += 0

print (sum)