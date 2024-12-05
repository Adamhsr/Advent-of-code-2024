with open('./day_5/input.txt', 'r') as file:
    inp = file.read().split("\n\n")

from functools import cmp_to_key

result = 0

top = set(inp[0].split("\n"))

bottom = inp[1].split("\n")

def check(a, b):
    return not (b + "|" + a) in top

def checklist(lst):
    works = True
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            works = works and check(lst[i], lst[j])
    return works

def sort2(a, b):
    if check(a, b):
        return 1
    return -1


for update in bottom:
    u = update.split(',')
    works = True
    for i in range(len(u)):
        for j in range(i, len(u)):
            works = works and check(u[i], u[j])
    if not works:
        result += int( sorted(u, key=cmp_to_key(sort2))[len(u)//2])



print(result)

