from datetime import datetime

hs, he, ms, me = map(int, input().split())

s1 = f'{hs}:{ms}'
s2 = f'{he}:{me}'
FMT = '%H:%M'

tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
print(tdelta)