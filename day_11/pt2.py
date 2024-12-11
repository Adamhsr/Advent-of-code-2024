with open('./day_11/input.txt', 'r') as file:
    inp = file.read().split()

stones = {}

for stone in inp:
    if stone in stones:
        stones[stone] = stones[stone] + 1
    else:
        stones[stone] = 1

for i in range(75):
    # print(stones)

    new_stones = {}
    for stone, num in stones.items():
        if stone == "0":
            if "1" in new_stones:
                new_stones['1'] += num
            else:
                new_stones['1'] = num
        elif len(stone) % 2 == 0:
            if str(int(stone[:len(stone) // 2])) in new_stones:
                new_stones[str(int(stone[:len(stone) // 2]))] += num
            else:
                new_stones[str(int(stone[:len(stone) // 2]))] = num
            if str(int(stone[len(stone) // 2:])) in new_stones:
                new_stones[str(int(stone[len(stone) // 2:]))] += num
            else:
                new_stones[str(int(stone[len(stone) // 2:]))] = num
        else:
            if str(int(stone) * 2024) in new_stones:
                new_stones[str(int(stone) * 2024)] += num
            else:
                new_stones[str(int(stone) * 2024)] = num
    stones = new_stones


s = 0
for num in stones.values():
    s += int(num)
print(s)