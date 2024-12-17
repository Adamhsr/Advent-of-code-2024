with open('./day_17/input.txt', 'r') as file:
    inp = file.read().split("\n\n")

instructions = list(map(int, inp[1][9:].split(",")))

instructions = list(reversed(instructions))

def run(a):
    res = []
    A = a
    B = 0
    C = 0
    while A > 0:
        B = A % 8
        B = B ^ 5
        C = A // (2**B)
        B = B ^ 6
        A = A // 8
        B = B ^ C
        res.append(B % 8)
    return res

def to_num(A):
    res = 0
    for i in range(len(A)):
        res += A[i] * (8**(len(A) - i - 1))
    return res

A = [1]
i = 0
while True:
    if A[i] == 7:
        A.pop()
        i -= 1
        A[i] += 1
        continue

    r = list(reversed(run(to_num(A))))

    if r[i] == instructions[i]:
        if len(r) == len(instructions):
            print(to_num(A))
            exit()
        A.append(0)
        i += 1
    else:
        A[i] += 1
