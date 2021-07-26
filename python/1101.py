m, n = map(int, input().split())

while m > 0 and n > 0:
    menor, maior = 0, 0

    if m > n:
        maior = m
        menor = n
    else:
        maior = n
        menor = m

    _list = []
    for num in range(menor, maior+1):
        _list.append(num)

    _sum = sum(_list)

    sorted_list = sorted(_list)

    print(*sorted_list, f"Sum={_sum}")

    m, n = map(int, input().split())