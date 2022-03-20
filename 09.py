# 제너레이터 함수

# Generator 는 iterator 객체의 한 종류

# 예

def gen_num():
    print('first number')
    yield 1 # yield 가 하나라도 들어가면 제너레이터가 됩니다.
    print('second number')
    yield 2
    print('third number')
    yield 3

gen = gen_num()

print(type(gen)) # generator객체

# generator 객체를 전달하면서 next 함수를 호출하면 함수의 첫 번재 문장부터 시작해서 첫번째 yield문을 만날 때 까지 실행을 이어간다. 그리고 이 때 yield 는 return 의 역할을 하게 되어 숫자 1을 반환한다.

next(gen)
next(gen)
next(gen)
# next(gen)  # stop iteration 에러 발생

# generator의 장점 : 메모리 공간을 적게 사용한다.

# yield from

def get_nums():
    ns = [0, 1, 0, 1, 0, 1]
    for i in ns:
        yield i

g = get_nums()
next(g)

# 위는 아래와 동일하다 for을 from으로 변경하여 사용

def get_nums2():
    ns2 = [0, 1, 0, 1, 0, 1]
    yield from ns2

g2 = get_nums2()
next(g2)

# **** 객체가 차지하는 메모리 공간의 크기 확인 sys.getsizeof()

import sys
print(sys.getsizeof(g2))