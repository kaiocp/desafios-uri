number_list = []
for number in range(0, 6):
    number = float(input())
    number_list.append(number)

pos_values = 0
for number in number_list:
    if number > 0:
        pos_values += 1

print(f"{pos_values} valores positivos")
