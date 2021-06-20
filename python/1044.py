a, b = map(int, input().split())

values = [a, b]
sorted_values = sorted(values)

if (sorted_values[1] % sorted_values[0] == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")
