def checks_cod():
    x = int(input())
    if 1 <= x <= 4:
        return x
    else:
        return checks_cod()


cod = int(input())

alc, gas, die = 0, 0, 0
while cod != 4:
    if cod == 1:
        alc += 1
    if cod == 2:
        gas += 1
    if cod == 3:
        die += 1

    cod = checks_cod()

print("MUITO OBRIGADO\n"
      f"Alcool: {alc}\n"
      f"Gasolina: {gas}\n"
      f"Diesel: {die}")

