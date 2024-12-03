with open('./day_1/input.txt', 'r') as file:
    inp = file.read().splitlines()

first = []
second = []


for line in inp:
    (f, s) = map( lambda x: int(x), line.split())
    first.append(f)
    second.append(s)

count = sum(e * second.count(e) for e in first)

print(count)