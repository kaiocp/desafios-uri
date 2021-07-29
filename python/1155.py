list1 = []

for i in range(2, 101):
    list1.append(i)

S = 1

for j in list1:
    S += 1 / j

print("{:.2f}".format(S))
