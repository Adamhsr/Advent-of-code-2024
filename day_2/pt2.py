with open('./day_2/input.txt', 'r') as file:
    inp = file.read().splitlines()

safe = 0

def check(report):
    
    checks = True
    last = report[0]
    change = 0
    for level in report[1:]:
        l = int(level)
        next_change = int(last) - int(l)
        if next_change == 0 or abs(next_change) > 3:
            checks = False
        if (change < 0 and next_change > 0) or (change > 0 and next_change < 0):
            checks = False
        last = level
        change = next_change
    
    if checks:
        return 1
    return 0


for report in inp:
    rep = list(map(lambda x: int(x), report.split()))
    checks = 0
    for i in range(len(rep)):
        checks += check(rep[0:i] + rep[i + 1:])
    
    if checks > 0:
        safe += 1

print(safe)