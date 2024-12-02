with open('./day_1/input.txt', 'r') as file:
    inp = file.read().splitlines()

first = []
second = []


for line in inp:
    (f, s) = map( lambda x: int(x), line.split())
    first.append(f)
    second.append(s)

count = 0

for elmn in first:
    count += elmn * second.count(elmn)

print(count)