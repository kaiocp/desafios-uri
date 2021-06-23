start, end = map(int, input().split())

total = 0

if (start > end):
    total = (24 - start) + end
elif (start < end):
    total = end - start
else:
    total = 24

print(f"O JOGO DUROU {total} HORA(S)")
