# 제너레이터 표현식

# 하나의 문장으로 제너레이터를 구성하는 방법

# 제너레이터 표현식은 제너레이터 함수와 마찬가지로 제너레이터 객체를 생성하는 방법이다.
# 제너레이터 표현식의 문법 구성이 리스트 컴프리헨션과 거의 똑같다.

def show_all(s):
    for i in s:
        print(i, end = ' ')

st = [2 * i for i in range(1, 10)]
show_all(st)

# 제너레이터로 작성

def times2():
    for i in range(1, 10):
        yield 2 * i
g = times2()
show_all(g)

g1 = [2 * i for i in range(1, 10)] # list comprehension 표현식
g2 = (2 * i for i in range(1, 10)) # 제너레이터 표현식
# [...]에서 (...)으로만 변경

print(next(g2))
print(next(g2))
print(next(g2))

def two():
    print('two')
    return 2

g = (two() * i for i in range(1, 10))
print(next(g))
print(next(g))
print(next(g))
