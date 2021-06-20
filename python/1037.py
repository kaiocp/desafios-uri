ent = float(input())

if ((ent >= 0) and (ent <= 25)):
    print("Intervalo [0,25]")
elif ((ent > 25) and (ent <= 50)):
    print("Intervalo (25,50]")
elif ((ent > 50) and (ent <= 75)):
    print("Intervalo (50,75]")
elif ((ent > 75) and (ent <= 100)):
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
