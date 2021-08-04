vet = []

for i in range(0, 10):
    x = int(input())
    if x <= 0:
        x = 1
    vet.append(x)

pos = 0
for j in vet:
    print(f"X[{pos}] = {j}")
    pos += 1
