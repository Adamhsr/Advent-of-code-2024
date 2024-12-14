with open("./day_14/input.txt", "r") as f:
    inp = f.read().split("\n")

from time import sleep
import re
robots = []
lx = 101
ly = 103

for robot in inp:
    robots.append(list(map(int, re.findall(r'-*\d+', robot))))


for _ in range(100):
    new_robots = []
    for robot in robots:
        x, y, dx, dy = robot
        x += dx
        y += dy
        if x < 0:
            x += lx
        if x >= lx:
            x -= lx
        if y < 0:
            y += ly
        if y >= ly:
            y -= ly
        new_robots.append([x, y, dx, dy])
    robots = new_robots

quads = [0,0,0,0]

for robot in new_robots:
    x, y, dx, dy = robot
    if x < lx//2 and y < ly//2:
        quads[0] += 1
    if x > lx//2 and y < ly//2:
        quads[1] += 1
    if x < lx//2 and y > ly//2:
        quads[2] += 1
    if x > lx//2 and y > ly//2:
        quads[3] += 1


from functools import reduce
print(reduce(lambda x, y: x*y, quads, 1))