with open('./day_3/input.txt', 'r') as file:
    inp = file.read()

import re

x = re.findall("mul\(\d*,\d*\)|don't\(\)|do\(\)", inp)

sum = 0
on = True
for y in x:
    if y  == "don't()":
        on = False
        continue
    if y == "do()":
        on = True
        continue
    if on:
        sum += int(y.split(',')[0].split("mul(")[1]) * int(y.split(',')[1].split(")")[0])

print(sum)