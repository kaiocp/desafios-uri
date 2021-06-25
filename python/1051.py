sallary = float(input())

tax_index = {
    sallary <= 2000: "Isento",
    (sallary > 2000) and (sallary <= 3000): 0.08,
    (sallary > 3000) and (sallary <= 4500): 0.18,
    sallary > 4500: 0.28
}

# Lembre que, se o salário for R$ 3002.00, a taxa que incide é de 8% apenas
# sobre R$ 1000.00, pois a faixa de salário que fica de R$ 0.00 até R$ 2000.00
# é isenta de Imposto de Renda. No exemplo fornecido (abaixo), a taxa é de
# 8% sobre R$ 1000.00 + 18% sobre R$ 2.00, o que resulta em R$ 80.36 no total
# esse babado aí de cima talvez me faça ter que pensar em outro codigo
