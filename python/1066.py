# storing values
_list = []
for num in range(5):
    num = int(input())
    _list.append(num)

# counting evens and odds
evens, odds = 0, 0
for num in _list:
    if num % 2 == 0:
        evens += 1
    else:
        odds += 1

# counting positives and negatives
pos, neg = 0, 0
for num in _list:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1

print(f"{evens} valor(es) par(es)\n"
      f"{odds} valor(es) impar(es)\n"
      f"{pos} valor(es) positivo(s)\n"
      f"{neg} valor(es) negativo(s)")