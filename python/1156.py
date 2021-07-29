lis1 = []
for i in range(3, 40, 2):
    lis1.append(i)

lis2 = []
aux = 1
for i in range(len(lis1)):
    aux *= 2
    lis2.append(aux)

S = 1

for a, b in zip(lis1, lis2):
    S += (a / b)

print("{:.2f}".format(S))
