with open("./day_13/input.txt", "r") as f:
    games = f.read().split("\n\n")

import re

total = 0

for game in games:
    lines = game.split("\n")
    a = list(map(int, re.findall(r'\d+', lines[0])))
    b = list(map(int, re.findall(r'\d+', lines[1])))
    t = list(map(int, re.findall(r'\d+', lines[2])))

    min_presses = -1

    As = Bs = 0

    while a[0] * As <= t[0] and a[1] * As <= t[1]:
        Bs = 0
        
        while a[0] * As + b[0] * Bs <= t[0] and a[1] * As + b[1] * Bs <= t[1]:
            if a[0] * As + b[0] * Bs == t[0] and a[1] * As + b[1] * Bs == t[1]:
                if min_presses == -1 or As * 3 + Bs < min_presses:

                    print(As, Bs, a, b, t)
                    min_presses = As * 3 + Bs
            Bs += 1
        As += 1
    
    if min_presses >= 0:
        total += min_presses

print(total)