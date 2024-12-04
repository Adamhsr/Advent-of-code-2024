with open('./day_4/input.txt', 'r') as file:
    inp = file.readlines()

sum = 0

for x in range(1, len(inp) - 1):
    for y in range(1, len(inp[0]) - 2):
        if inp[x][y] != "A":
            continue
        if (inp[x+1][y+1] == "M" and inp[x-1][y-1] == "S") or (inp[x+1][y+1] == "S" and inp[x-1][y-1] == "M"):
            if (inp[x+1][y-1] == "M" and inp[x-1][y+1] == "S") or (inp[x+1][y-1] == "S" and inp[x-1][y+1] == "M"):
                sum += 1

print (sum)