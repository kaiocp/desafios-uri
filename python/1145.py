x, y = map(int, input().split())

i = 1

while i != y+1:
    counter = 0
    for a in range(0, x):
        if counter == x - 1:
            print(i)
        else:
            print(i, end=' ')
        i += 1
        counter += 1
