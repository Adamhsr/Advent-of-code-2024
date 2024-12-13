with open("./day_13/input.txt", "r") as f:
    games = f.read().split("\n\n")

import re

total = 0

for game in games:
    lines = game.split("\n")
    a = list(map(int, re.findall(r'\d+', lines[0])))
    b = list(map(int, re.findall(r'\d+', lines[1])))
    t = list(map(lambda x: 10000000000000 + int(x), re.findall(r'\d+', lines[2])))

    # just solve the system of equasions
    As = int((t[1]*b[0]-b[1]*t[0]) / (a[1]*b[0]-b[1]*a[0]))
    Bs = int(t[0]/b[0] - (As) * (a[0]/b[0]))


    # floating point errors
    for eA in range(-3, 3):
        for eB in range(-3, 3):
            if As >= 0 and Bs >= 0:
                if a[0] * (As + eA) + b[0] * (Bs + eB) == t[0] and a[1] * (As + eA) + b[1] * (Bs + eB) == t[1]:
                    total += (As + eA) * 3 + (Bs + eB)

print(total)