with open('./day_1/input.txt', 'r') as file:
    inp = file.read().splitlines()

first = []
second = []


for line in inp:
    (f, s) = map( lambda x: int(x), line.split())
    first.append(f)
    second.append(s)

first.sort()
second.sort()

count = 0

for i in range(len(first)):
    count += abs(first[i] - second[i])

print(count)