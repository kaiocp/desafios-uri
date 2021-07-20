n = int(input())

p1, p2, p3, = 2, 3, 5

for i in range(n):
    v1, v2, v3 = map(float, input().split())
    avg = ((v1*p1)+(v2*p2)+(v3*p3)) / (p1+p2+p3)
    print("{:.1f}".format(avg))




