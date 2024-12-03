with open('./day_3/input.txt', 'r') as file:
    inp = file.read()

import re

x = re.findall("mul\(\d*,\d*\)", inp)

s = 0
for y in x:
    s += int(y.split(',')[0].split("mul(")[1]) * int(y.split(',')[1].split(")")[0])

print(sum(int(e.split(',')[0].split("mul(")[1]) * int(y.split(',')[1].split(")")[0] for y in x)))

print(s)