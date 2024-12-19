with open('./day_19/input.txt', 'r') as file:
    inp = file.read().split("\n\n")

patterns = inp[0].split(", ")

from functools import cache

@cache
def possibilities(towel):
    if len(towel) == 0:
        return 1
    num = 0
    for pattern in patterns:
        if towel.startswith(pattern):
            num += possibilities(towel[len(pattern):])
    return num


print(sum(possibilities(towel) for towel in inp[1].split("\n")))