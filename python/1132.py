x = int(input())
y = int(input())

_sum = 0

if x > y:
    for i in range(y, x+1):
        if i % 13 == 0:
            continue
        else:
            _sum += i

if x < y:
    for i in range(x, y+1):
        if i % 13 == 0:
            continue
        else:
            _sum += i

print(_sum)