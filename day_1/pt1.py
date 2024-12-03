with open('./day_1/input.txt', 'r') as file:
    inp = file.readlines()

first = []
second = []

for line in inp:
    (f, s) = map( int, line.split())
    first.append(f)
    second.append(s)

first.sort()
second.sort()

count = sum(abs(a - b) for a, b in zip(first, second))

print(count)