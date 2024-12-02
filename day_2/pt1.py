with open('./day_2/input.txt', 'r') as file:
    inp = file.read().splitlines()

safe = 0

for report in inp:
    checks = True
    last = int(report.split()[0])
    change = 0
    for level in report.split()[1:]:
        l = int(level)
        next_change = int(last) - int(l)
        if next_change == 0 or abs(next_change) > 3:
            checks = False
        if (change < 0 and next_change > 0) or (change > 0 and next_change < 0):
            checks = False
        last = level
        change = next_change
    
    if checks:
        safe += 1

print(safe)