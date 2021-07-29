x = int(input())

_sum = 0
counter = 0

while x >= 0:
    _sum += x
    counter += 1
    x = int(input())

_avg = _sum / counter

print(f"{_avg:.2f}")
