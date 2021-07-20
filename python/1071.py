x = int(input())
y = int(input())
_sum = 0

# if the first one is lesser than the second
if x < y:
    for i in range(x+1, y):
        if i % 2 != 0:
            _sum += i

# if the first one is greater than the second
elif x > y:
    for i in range(y+1, x):
        if i % 2 != 0:
            _sum += i

print(_sum)