codigo, quantidade = input().split()
codigo = int(codigo)
quantidade = int(quantidade)

if (codigo == 1):
    valor = 4.0
if (codigo == 2):
    valor = 4.5
if (codigo == 3):
    valor  = 5.0
if (codigo == 4):
    valor = 2.0
if (codigo == 5):
    valor = 1.5

total = valor * quantidade

print(f"Total: R$ {total:.2f}")
