i, j = -1, 7

while i != 11 and j != 17:
    i += 2
    for a in range(0, 3):
        print(f"I={i} J={j}")
        j -= 1
    j += 5

