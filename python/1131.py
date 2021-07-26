def checks_continue():
    x = int(input("Novo grenal (1-sim 2-nao)\n"))
    return x


_continue = 1
gr_wins, in_wins, ties = 0, 0, 0
total_grenais = 0

while _continue == 1:
    in_goals, gr_goals = map(int, input().split())

    if gr_goals > in_goals:
        gr_wins += 1
    elif gr_goals < in_goals:
        in_wins += 1
    else:
        ties += 1

    total_grenais += 1

    _continue = checks_continue()

print(f"{total_grenais} grenais\n"
      f"Inter:{in_wins}\n"
      f"Gremio:{gr_wins}\n"
      f"Empates:{ties}")

if gr_wins > in_wins:
    print("Gremio venceu mais")
elif gr_wins < in_wins:
    print("Inter venceu mais")
else:
    print("Nao houve vencedor")




