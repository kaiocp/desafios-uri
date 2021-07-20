n = int(input())

tot_cobaias, tot_c, tot_r, tot_s = 0, 0, 0, 0

for i in range(n):
    qnt, tip = map(str, input().split())
    qnt = int(qnt)

    tot_cobaias += qnt

    if tip == 'C':
        tot_c += qnt
    if tip == 'R':
        tot_r += qnt
    if tip == 'S':
        tot_s += qnt

pc_c = (tot_c * 100) / tot_cobaias
pc_r = (tot_r * 100) / tot_cobaias
pc_s = (tot_s * 100) / tot_cobaias

print(f"Total: {tot_cobaias} cobaias\n"
      f"Total de coelhos: {tot_c}\n"
      f"Total de ratos: {tot_r}\n"
      f"Total de sapos: {tot_s}\n"
      f"Percentual de coelhos: {pc_c:.2f} %\n"
      f"Percentual de ratos: {pc_r:.2f} %\n"
      f"Percentual de sapos: {pc_s:.2f} %")
