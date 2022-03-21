# 튜플의 패킹과 언패킹

# 튜플 패킹 : 하나 이상의 값을 튜플로 묶는 행위
# 튜플 언패킹 : 튜플에 묶여 있는 값들을 풀어내는 행위

tri_one = (12, 15) # 삼각형 밑변과 높이의 길이를 묶어 놓은 것
print(tri_one)

tri_two = 23, 12 # 소괄호가 없어도 패킹이 된다.
print(tri_two)

tri_three = (12, 25)
bt, ht = tri_three # 튜플 언패킹
print(bt, ht)

nums = (1, 2, 3, 4, 5)

n1, n2, *others = nums #  둘 이상의 값을 리스트로 묶을 때 *를 사용한다.
print(n1) # 1
print(n2) # 2
print(others) # [3, 4, 5] 튜플이 아닌 리스트로 묶인다.

# 리스트에서도 언패킹 된다.

nums = [1, 2, 3, 4, 5]
n1, n2, *others = nums

print(n1)
print(n2)
print(others)

def ret_nums():
    return 1, 2, 3, 4, 5 #  튜플의 소괄호가 생략된 형태, 즉 패킹되어 반환된다.

nums = ret_nums()
print(nums)

def show_nums(n1, n2, *other): # 세번째 이후 값들은 튜플로 묶여 other에 전달 => 매개변수에 *가 오면 튜플로 묶어서 저장
    print(n1, n2, other, sep = ',')

show_nums(1, 2, 3, 4)
show_nums(1, 2, 3, 4, 5)

# 매개변수에 *가 오면 나머지 값들은 튜플로 묶어서 이 변수에 저장하겠다는 의미

def sum(*nums):
    s = 0
    for i in nums:
        s+=i
    return s

print(sum(1, 2, 3, 6, 7, 9))

# 함수를 호출할 때 '*'가 사용되면 이는 튜플 언패킹으로 이어진다. 이렇듯 *은 사용되는 위치에 따라서 패킹을 의미하기도, 언패킹을 의미하기도 한다.
def show_man(name, age, height):
    print(name, age, height, sep = ',')

p = ('Yoon', 22, 190)
# show_man(p)
show_man(*p) # 언패킹후 함수 대입

# for 루프에서의 언패킹

ps = [('Lee', 172), ('Jung', 182), ('Yoon', 179)]  # list에 담긴 튜플
for n, h in ps:
    print(n, h, sep = ', ')
