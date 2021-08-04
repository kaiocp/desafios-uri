n = int(input())

i = 0
while i < n:
    fatores = []

    x = int(input())

    for j in range(x-1, 0, -1):
        if x % j == 0:
            fatores.append(j)

    summ = sum(fatores)

    if summ == x:
        print(f"{x} eh perfeito")
    else:
        print(f"{x} nao eh perfeito")

    i += 1

