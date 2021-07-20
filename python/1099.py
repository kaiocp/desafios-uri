n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    _sum = 0

    if x > y:
        if (x % 2 == 0) and (y % 2 == 0):
            for j in range(y+1, x):
                if j % 2 != 0:
                    _sum += j
        elif (x % 2 == 0) and (y % 2 != 0):
            for j in range(y+2, x):
                if j % 2 != 0:
                    _sum += j
        elif (x % 2 != 0) and (y % 2 == 0):
            for j in range(y+1, x):
                if j % 2 != 0:
                    _sum += j
        else:
            for j in range(y+2, x):
                if j % 2 != 0:
                    _sum += j

    elif x < y:
        if (x % 2 == 0) and (y % 2 == 0):
            for j in range(x+1, y):
                if j % 2 != 0:
                    _sum += j
        elif (x % 2 == 0) and (y % 2 != 0):
            for j in range(x+1, y):
                if j % 2 != 0:
                    _sum += j
        elif (x % 2 != 0) and (y % 2 == 0):
            for j in range(x+2, y):
                if j % 2 != 0:
                    _sum += j
        else:
            for j in range(x+2, y):
                if j % 2 != 0:
                    _sum += j

    print(_sum)
