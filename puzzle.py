#https://aoc.infi.nl/2024

with open('./input.txt', 'r') as file:
    inp = file.read().split("\n")

from time import time
from collections import deque

def execute(pos):
    pc = 0
    stack = []
    while True:
        ins = inp[pc]
        pc += 1
        if ins[0:4] == "push":
            if ins[5] == "X":
                 stack.append(pos[0])
            elif ins[5] == "Y":
                stack.append(pos[1])
            elif ins[5] == "Z":
                stack.append(pos[2])
            else:
                stack.append(int(ins[5:]))
        elif ins[0:3] == "add":
            stack.append(stack.pop() + stack.pop())
        elif ins[0:5] == "jmpos":
            if stack[-1] >= 0:
                pc += int(ins[6:])
        elif "ret" in ins:
            return stack.pop()

t = time()

neighbors_offsets = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

unchecked = set()
blocks = 0
clouds = 0

for x in range(30):
    for y in range(30):
        for z in range(30):
            pos = (x, y, z)
            if execute(pos) > 0:
                unchecked.add(pos)
                blocks += 1

checking = deque()

while unchecked:
    # Start with an unchecked position to begin a new cloud
    if len(checking) == 0:
        checking.append(unchecked.pop())
        clouds += 1

    # Get the next block to check
    pos = checking.pop()

    # Explore the neighbors of this block
    for dx, dy, dz in neighbors_offsets:
        neighbor_pos = (pos[0] + dx, pos[1] + dy, pos[2] + dz)
        if neighbor_pos in unchecked:
            unchecked.remove(neighbor_pos)
            checking.append(neighbor_pos)


print(f"\nThere are {blocks} blocks of snow, making up {clouds} clouds.")
print(f"Computed time: {1000 * (time() - t)}ms\n")