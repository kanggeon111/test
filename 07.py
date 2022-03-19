# 07.py map & filter

# map

def pow(n):
    return n ** 2 # n의 제곱 값을 계산해서 반환

st1 = [1, 2 ,3]
st2 = [pow(st1[0]), pow(st1[1]), pow(st1[2])]

# 위 코드는 불편하므로 map을 이용해서 바꾼다.

st3 = list(map(pow, st1)) # map은 st1의 값을 전달하면서 pow를 호출
print(st3)

def db1(e):
    return e *2

print(list(map(db1, (1, 3, 4))))
print(list(map(db1, 'hello')))

def sum (n1, n2):
    return n1 + n2

st1 = [1, 2, 3]
st2 = [3, 2, 1]
print(list(map(sum, st1, st2)))

st = [1, 2, 3, 4, 5, 6, 7, 8]

print(st [ : ])
print(st [ : :1])
print(st [ : :2])
print(st [ : :3])
print(st [ : :-1])

s = 'hello'
print(s[::-1])

# list에 담긴 문자열들을 모두 뒤집어서 새 리스트에 담는 코드
def rev(s):
    return s[ : : -1]

st = ['one', 'two', 'three']
rst = list(map(rev, st))
print(rst)

# 람다 적용
rst2 = list(map(lambda s : s[: : -1], st))
print(rst2)

# filter
#filter도 함수를 인자로 받는다. 값을 걸러내는 기능을 제공

def is_odd(n):
    return n % 2 # 홀수이면 True 반환

st = [1, 2 ,3, 4, 5]
ost = list(filter(is_odd, st))
print(ost)

#Filter 함수는 True 또는 False를 반환하는 함수여야 한다.

ost2 = list(filter(lambda n : n%2, st))
print(ost2)

# 10이하 자연수 중 3의 배수만 리스트에 담기
st = list(range(1, 11))
fst = list(filter(lambda s : not(s%3), st))
print(fst)

# map과 filter를 모두 사용하기
# 1 ~ 10의 제곱을 리스트에 담되 3의 배수만 담기
st = list(range(1, 11))
ast = list(filter(lambda s : not(s % 3), map(lambda j : j**2, st)))
print(ast)