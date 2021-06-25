ddd = {
    61: "Brasilia",
    71: "Salvador",
    11: "Sao Paulo",
    21: "Rio de Janeiro",
    32: "Juiz de Fora",
    19: "Campinas",
    27: "Vitoria",
    31: "Belo Horizonte"
}

ddd_inpt = int(input())

if ddd_inpt in ddd:
    print(ddd[ddd_inpt])
else:
    print("DDD nao cadastrado")
