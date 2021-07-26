# i = -0.2
# j = 0
#
# conv = i == 0.0
#
# counter = 0
# while counter < 12:# i != 2.2:
#     i += 0.2
#     j = 0
#     j += i
#     for a in range(3):
#         j += 1
#         if conv:
#             print(f"I={int(i)} J={int(j)}")
#         else:
#             print(f"I={i} J={j}")
#     counter += 1

i = 0
j = 1

while i != 2.2:
    for a in range(3):
        print(f"I={i} J={j}")
        j += 1 + i
    i += 0.2


