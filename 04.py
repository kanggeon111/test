# list comprehension : for 루프를 사용하지 않는 형태

# list 생성 방법
r1 = [1, 2, 3]
r2 = []
r3 = [1, 2, [3, 4]]

r4 = list('hello')
r5 = list((5, 6, 7))
r6 = list(range(0, 6))

t1 = list(range(1, 6))
s = []
for i in t1:
    s.append(i * 2)
print(s)

t2 = [1, 2, 3, 4, 5]
t3 = [x * 2 for x in t2]
print(t3)

# [1, 2, 3, 4, 5]의 모든 값을 10씩 증가
t4 = [1, 2, 3, 4, 5]
t5 = [x + 10 for x in t4]
print(t5)

# if 추가
t6 = [1, 2, 3, 4, 5]
s1 = []
for i in t6:
    if i%2 == 1:
        s1.append(i * 2)
print(s1)

s2 = []
s3 = [x*2 for x in t6 if x % 2]
print(s3)

# 이중 for문
i1 = ['Black', 'White']
i2 = ['Red', 'Blue', 'Green']
i3 = []

for i in i1:
    for j in i2:
        i3.append(i+j)
print(i3)

i4 = [i + j for i in i1 for j in i2]
print(i4)