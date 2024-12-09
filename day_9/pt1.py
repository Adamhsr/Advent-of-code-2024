with open('./day_9/input.txt', 'r') as file:
    inp = list(file.read())

result = 0
pos = 0

space = []

for i, n in enumerate(inp):
    if i % 2 == 1:
        space = space + [-1] * int(n)
    else:
        space = space + [int(i/2)] * int(n)

new = []
no_zeros = list(filter(lambda x: x >= 0, space))

for i in range(len(no_zeros)):
    if space[i] == -1:
        new.append(no_zeros.pop())
    else:
        new.append(space[i])

for i, n in enumerate(new):
    result += i * n
print(result)
