# 함수 호출과 매개변수 선언에 있어서 *와 **의 사용 규칙

# func(*iterable) : iterable 객체를 전달하면서 *을 붙여서 함수 호출할 때  -- (1)
# func(**dict) : dict객체를 전달하면서 **을 붙여서 함수 호출할 때
# def func(*args) : 함수를 정의하면서 매개변수 args에 *을 붙일 때
# def func(**args) : 함수를 정의하면서 매개변수 args에 **을 붙일 때

# (1)
def who(a, b, c):
    print(a, b, c, sep = ',')

who(*[1, 2, 3]) # 리스트를 풀어서 매개변수에 각각 전달

who(*(0.1, 0.2, 0.3)) # 튜플을 풀어서 매개변수에 각각 전달

who(*'abc') # 문자열을 풀어서 매개변수에 각각 전달

# (2)
d = dict(a = 1, b = 2, c = 3)
who(*d)  # *을 붙이면 키가 매개변수에 전달
who(**d) # **을 붙이면 값이 매개변수에 전달

who(*d.items()) # 키와 값을 묶어서 전달

# (3)
def func(*args):
    print(args) # args는 튜플

func() # 빈 튜플이 전달
func(1) # 1이 튜플로 묶여서 전달
func(1, 2) # 1과 2가 튜플로 묶여서 전달
func(1, 2, 3)

# (4) key = value의 형태로 전달해야 한다.
def func2(**args):
    print(args) # args는 딕셔너리

func2(a = 1) #
func2(a = 1, b = 2)
func2(a=1, b= 2, c = 3)

# *args와 **args를 동시에 둘 수 있다.
def func2(*args1, **args2):
    print(args1) # args1은 튜플
    print(args2) # args2는 딕셔너리

func2()
func2(1, a = 1)
func2(1, 2, a = 1, b = 2)
