n = int(input())

# if n is even:
if n % 2 == 0:
    for num in range(2, n+1, 2):
        print(f"{num}^2 =", pow(num, 2))

# if in is odd:
else:
    for num in range(2, n, 2):
        print(f"{num}^2 =", pow(num, 2))

