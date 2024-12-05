with open('./day_5/input.txt', 'r') as file:
    inp = file.read().split("\n\n")

result = 0

top = inp[0].split("\n")

def check(a, b):
    for line in top:
        p1, p2 = line.split("|")
        if p2 == a and p1 == b:
            return False
    return True

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


