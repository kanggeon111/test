# s = 'Garbage collection'
#
# print(s)

# immutable & mutable

r = [1, 2]

a = id(r)  # list 의 주소 정보 확인
print(a)

r += [3, 4]
b = id(r)
print(b) #  list의 주소 변경 x

t = (1, 2)
c = id(t)
print(c)

t += (3, 4)
d = id(t)
print(d) # 새로운 주소 설정

def add_last(m ,n):
    m += n

r = [1, 2]

add_last(r, [3, 4])
print(r)

s = (1, 2)
add_last(s, (3, 4))
print(s) # 튜플은 추가 x

def add_tuple(m, n):
    m+=n
    return m

j = add_tuple(s, (3, 4)) # 새로운 튜플 생성
print(j)

ex = [1, 2, 3, 5, 7, 9]
print(ex[-1])

# 정리 : immutable - 문자열, tuple, mutable - list, dictionary
