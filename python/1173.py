x = int(input())

n = [x]

for i in range(0, 9):
    x *= 2
    n.append(x)

pos = 0

for j in n:
    print(f"N[{pos}] = {j}")
    pos += 1

