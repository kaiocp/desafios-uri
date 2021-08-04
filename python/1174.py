a = []

for i in range(0, 100):
    x = float(input())
    a.append(x)

pos = 0

for j in a:
    if j <= 10:
        print(f"A[{pos}] = {j}")
    pos += 1


