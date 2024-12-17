with open('./day_17/input.txt', 'r') as file:
    inp = file.read().split("\n\n")

import re

A, B, C = list(map(int, re.findall(r"\d+", inp[0])))

instructions = list(map(int, re.findall(r"\d+", inp[1])))


def run(A, B, C, instructions):
    ptr = 0
    output_num = 0

    def combo(operand):
        if operand == 4:
            return A
        if operand == 5:
            return B
        if operand == 6:
            return C
        return operand

    while ptr < len(instructions):
        opcode = instructions[ptr]
        operand = instructions[ptr + 1]

        match opcode:
            case 0:
                A = A // (2**combo(operand))
            case 1:
                B = B ^ operand
            case 2:
                B = combo(operand) % 8
            case 3:
                if A != 0:
                    ptr = combo(operand) - 2
            case 4:
                B = B ^ C
            case 5:
                if instructions[output_num] != combo(operand) % 8:
                    return False
                else:
                    output_num += 1
            case 6:
                B = A // (2**combo(operand))
            case 7:
                C = A // (2**combo(operand))

        ptr += 2
    return output_num == len(instructions)

i = 1087000000
while True:
    i += 1
    if i % 1000000 == 0:
        print(i)
    if run(i, B, C, instructions):
        print(i)
        exit()