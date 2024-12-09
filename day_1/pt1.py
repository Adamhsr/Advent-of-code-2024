with open('./day_1/input.txt', 'r') as file:
    inp = file.readlines()

first = []
second = []


first, second = map(list, list(zip(*((int(x) for x in line.split()) for line in inp))))


first.sort()
second.sort()

count = sum(abs(a - b) for a, b in zip(first, second))

print(count)