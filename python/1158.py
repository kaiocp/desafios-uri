n = int(input())

counter = 0

while counter < n:
    x, y = map(int, input().split())
    aux = y
    _sum = 0

    if x % 2 == 0:
        y = x + (aux*2)
        for i in range(x+1, y, 2):
            if i % 2 != 0:
                _sum += i

    else:
        y = x + (aux*2)
        for i in range(x, y, 2):
            if i % 2 != 0:
                _sum += i

    print(_sum)
    counter += 1
