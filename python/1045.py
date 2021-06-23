a, b, c = map(float, input().split())

_list = [a, b, c]

dec = sorted(_list, reverse=True) 

not_a_triangle = dec[0] >= dec[1] + dec[2]
rectangle_triangle = pow(dec[0], 2) == pow(dec[1], 2) + pow(dec[2], 2)
obtuse_triangle = pow(dec[0], 2) > pow(dec[1], 2) + pow(dec[2], 2) and not not_a_triangle
acute_triangle = pow(dec[0], 2) < pow(dec[1], 2) + pow(dec[2], 2) 
equilateral_triangle = (a == b) and (b == c) and (c == a)
isosceles_triangle = (a == b) or (b == c) or (c == a)

if not_a_triangle:
    print("NAO FORMA TRIANGULO")
if rectangle_triangle:
    print("TRIANGULO RETANGULO")
if obtuse_triangle:
    print("TRIANGULO OBTUSANGULO")
if acute_triangle:
    print("TRIANGULO ACUTANGULO")
if equilateral_triangle:
    print("TRIANGULO EQUILATERO")
if isosceles_triangle and not equilateral_triangle:
    print("TRIANGULO ISOSCELES")
