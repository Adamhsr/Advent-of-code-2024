with open('./day_7/input.txt', 'r') as file:
    inp = file.read().splitlines()

result = 0

def possible(test, values):
    if len(values) == 1:
        return test == values[0]
    if values[0] > test:
        return False
    return possible(test, [values[0] + values[1]] + values[2:]) or possible(test, [values[0] * values[1]] + values[2:]) or possible(test, [int(str(values[0]) + str(values[1]))] + values[2:])

for line in inp:
    tst, vls = line.split(":")
    tst = int(tst)
    vls = list(map(int, vls.split()))
    if possible(tst, vls):
        result += tst

print(result)