with open('./day_1/input.txt', 'r') as file:
    inp = file.read().splitlines()

first = []
second = []

first, second = list(zip(*((int(x) for x in line.split()) for line in inp)))

count = sum(e * second.count(e) for e in first)

print(count)