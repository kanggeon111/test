# 객체처럼 다뤄지는 함수 그리고 람다

# 파이썬에서는 함수도 객체
x = 3.0
print(type(x))
print(x.is_integer()) # 소수점 이하에 값이 있는지 묻는것

def func1(n):
    return n

print(type(func1)) # function이라는 클래스의 객체

def say1():
    print('hello')

def say2():
    print('Hi')

def caller(fct):
    fct()

caller(say1)

def fct_fac(n):
    def exp(x): # 함수 내에 정의돈, x의 n제곱을 반환하는 함수
        return x ** n
    return exp # 위에서 정의한 함수 exp를 반환

f2 = fct_fac(2) # 제곱을 계산해서 반환하는 함수를 참조
f3 = fct_fac(3) # 세제곱을 계산해서 반환하는 함수를 참조

print(f2(4))
print(f3(4))

# 람다 (이름없는 함수 정의)
# lambda args : expression -> 표현식
# 매개변수 선언을 args, 함수의 몸체 내용을 expression에 둔다.

def show(s):
    print(s)

ref = show
ref('~hi')

ref2 = lambda s : print(s) # 람다 기반의 함수 정의
ref('hi')

# 람다 함수의 매개변수는 s이다.
# s를 가지고 실행할 함수 몸체는 print(s) 이다.
# 이렇게 해서 생성된 함수를 ref에 저장한다.

f1 = lambda s1, s2 : s1 + s2
print(f1(2, 3))

f2 = lambda a : len(a)
print(f2('simple'))

def fct_fac(n):
    def exp(x): # 함수 내에 정의돈, x의 n제곱을 반환하는 함수
        return x ** n
    return exp # 위에서 정의한 함수 exp를 반환

# 이 식을 람다로 작성
def fct_fac_lambda(n):
    return lambda x : x ** n

ret2 = fct_fac_lambda(2)
ret3 = fct_fac_lambda(3)

print(ret2(4))

# 람다식은 보는 순간 쉽게 파악이 가능한 수준에서 작성하는 것이 좋다.

