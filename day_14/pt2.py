with open("./day_14/input.txt", "r") as f:
    inp = f.read().split("\n")

from time import sleep
import re
robots = []
lx = 101
ly = 103

for robot in inp:
    robots.append(list(map(int, re.findall(r'-*\d+', robot))))

for s in range(7083):

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

for y in range(ly):
            for x in range(lx):
                r = 0
                for robot in robots:
                    if robot[0] == x and robot[1] == y:
                        r += 1
                if r == 0:
                    print(" ", end="")
                else:
                    print(r, end="")
            print()