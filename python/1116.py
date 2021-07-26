qnt = int(input())

for i in range(qnt):
    x, y = map(int, input().split())
    try:
        div = x / y
        print(div)
    except ZeroDivisionError:
        print("divisao impossivel")