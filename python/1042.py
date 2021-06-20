a, b, c = map(int, input().split())

_list = [a, b, c]

sorted_list = sorted(_list)

for number in sorted_list:
    print(number)
print()
for number in _list:
    print(number)
