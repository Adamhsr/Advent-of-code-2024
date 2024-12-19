with open('./day_19/input.txt', 'r') as file:
    inp = file.read().split("\n\n")

patterns = inp[0].split(", ")

from functools import cache

@cache
def can_make(towel):
    if len(towel) == 0:
        return True
    for pattern in patterns:
        if towel.startswith(pattern):
            if can_make(towel[len(pattern):]):
                return True
    return False

print(len(list(filter(can_make, inp[1].split("\n")))))