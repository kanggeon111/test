# dict의 생성과 zip

# dict의 다양한 생성 방법

# 딕셔너리의 기본적인 생성 방법은 다음과 같다.
d = {'a' : 1, 'b' :2, 'c' : 3}

print(d)
print(type(d))

# 또 다른 딕셔너리 생성 방법
d2 = dict([('a', 1), ('b', 2), ('c', 3)])
print(d2)

# 딕셔너리의 키가 문자열인 경우에는 다음이 가능
d3 = dict(a = 1, b = 2, c = 3)
print(d3)

# 키는 키끼리 값은 값끼리 묶어서 생성 가능 이때 zip을 사용
d4 = dict(zip(['a', 'b', 'c'],[1, 2, 3]))
print(d4)

d5 = {'a' : 1, 'b' : 2, 'c' : 3}
d5['d'] = 4
print(d5)

# for k in d5:
#     print(d[k], end = ',')

# zip 함수

z = zip(['a', 'b', 'c'], [1, 2, 3])
for i in z:
    print(i, end = ', ')

z = zip('abc', (1, 2, 3))
for i in z:
    print(i, end = ', ')

c = list(zip('abc', (1, 2, 3), ['one', 'two', 'three']))
for i in c:
    print(i, end = ', ')