#https://aoc.infi.nl/2024

with open('./input.txt', 'r') as file:
    inp = file.read().split("\n")

from time import time

ans1 = 0
clouds = []


def execute():
    pc = 0
    stack = []
    while True:
        ins = inp[pc]
        pc += 1
        if ins[0:4] == "push":
            if ins[5] == "X":
                stack.append(X)
            elif ins[5] == "Y":
                stack.append(Y)
            elif ins[5] == "Z":
                stack.append(Z)
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

for X in range(30):
    for Y in range(30):
        for Z in range(30):
            if execute() > 0:
                ans1 += 1
                ## add neighbors of new clouds
                new_clouds = [{(X + 1, Y, Z), (X - 1, Y, Z),
                (X, Y + 1, Z), (X, Y - 1, Z),
                (X, Y, Z + 1), (X, Y, Z - 1)}]
                for neighbors in clouds:
                    if (X, Y, Z) in neighbors:
                        new_clouds[0] = new_clouds[0].union(neighbors)
                    else:
                        new_clouds.append(neighbors)
                
                clouds = new_clouds


print(f"\nThere are {ans1} blocks of snow, making up {len(clouds)} clouds.")
print(f"Computed time: {1000 * (time() - t)}ms\n")