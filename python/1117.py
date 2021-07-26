def checks_grade():
    x = float(input())
    if 0 <= x <= 10:
        return x
    else:
        print("nota invalida")
        return checks_grade()


n1 = checks_grade()
n2 = checks_grade()

_avg = (n1 + n2) / 2

print(f"media = {_avg:.2f}")
