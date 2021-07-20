i, j = 1, 7

while (i != 11) and (j != 5):
    print(f"I={i} J={j}")
    j -= 1
    if j == 5:
        print(f"I={i} J={j}")
        i += 2
        j = 7
