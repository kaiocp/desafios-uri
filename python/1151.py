n = int(input())

fib = [0, 1, 1]

for i in range(0, n-3):
    x = fib[-1] + fib[-2]
    fib.append(x)

print(*fib)