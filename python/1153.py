n = int(input())
n += 1

lis = []

for i in range(1, n):
    lis.append(i)

fat = 1

for i in lis:
    fat *= i

print(fat)