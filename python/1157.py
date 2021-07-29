x = int(input())

lis = []

for i in range(1, x+1):
    if x % i == 0:
        lis.append(i)

for i in lis:
    print(i)