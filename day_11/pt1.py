with open('./day_11/input.txt', 'r') as file:
    stones = file.read().split()



for i in range(75):
    # print(stones)

    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            new_stones.append(str(int(stone[:len(stone) // 2])))
            new_stones.append(str(int(stone[len(stone) // 2:])))
        else:
            new_stones.append(str(int(stone) * 2024))
    stones = new_stones

print(len(stones))