def checks_grade():
    x = float(input())
    if 0 <= x <= 10:
        return x
    else:
        print("nota invalida")
        return checks_grade()


def checks_cont():
    x = input("novo calculo (1-sim 2-nao)\n")
    if x != '1' and x != '2':
        return checks_cont()
    else:
        return x


cont = '1'

while cont != '2':
    n1 = checks_grade()
    n2 = checks_grade()

    _avg = (n1+n2) / 2

    print(f"media = {_avg:.2f}")

    cont = checks_cont()

