qnt = int(input())

_in = 0
_out = 0

for i in range(qnt):
    num = int(input())
    if 10 <= num <= 20:
        _in += 1
    else:
        _out += 1

print(f"{_in} in\n"
      f"{_out} out")

