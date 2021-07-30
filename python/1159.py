x = int(input())

while x != 0:
    _sum = 0
    aux = x + 10
    if x % 2 == 0:
        for i in range(x, aux, 2):
            _sum += i
    else:
        for i in range(x+1, aux, 2):
            _sum += i

    print(_sum)
    x = int(input())

