with open('./day_5/input.txt', 'r') as file:
    inp = file.read().split("\n\n")

result = 0

top = set(inp[0].split("\n"))

def check(a, b):
    return not (b + "|" + a) in top

bottom = inp[1].split("\n")

for update in bottom:
    u = update.split(',')
    works = True
    for i in range(len(u)):
        for j in range(i, len(u)):
            works = works and check(u[i], u[j])
    if works:
        result += int(u[len(u) // 2])

print(result)


