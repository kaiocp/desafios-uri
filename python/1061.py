number_list = []
for number in range(0, 6):
    number = float(input())
    number_list.append(number)

pos_numbers = 0
sum = 0
for number in number_list:
    if number > 0:
        pos_numbers += 1
        sum += number

avg = sum / pos_numbers

print(f"{pos_numbers} valores positivos")
print("{:.1f}".format(avg))
