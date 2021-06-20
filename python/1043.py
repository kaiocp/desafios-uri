a, b, c = map(float, input().split())

sides = [a, b, c]
sorted_sides = sorted(sides)

is_triangle = (sorted_sides[0] + sorted_sides[1]) > sorted_sides[2]

if is_triangle:
    perimeter = a + b + c
    print(f"Perimetro = {perimeter:.1f}")
else:
    area = ((a+b)*c) / 2
    print(f"Area = {area:.1f}")
