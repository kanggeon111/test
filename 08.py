# 08.py 두 함수를 대신하는 리스트 컴프리핸션

st1 = [1, 2, 3]

st2 = list(map(lambda n : n**2, st1))
print(st2)

st3 = [n**2 for n in st1]
print(st3)

st = [1, 2, 3, 4, 5]
ost = list(filter (lambda n : n% 2, st))
print(ost)

ost2 = [i for i in st if i % 2 == 1]
print(ost2)