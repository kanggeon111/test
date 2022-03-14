r1 = [1, 2, 3]
r2 = [1, 2, 3]

if r1 is r2:
    print("True")
else:
    print("False")

# v1 == v2 :  변수 v1과 v2가 참조하는 객체의 내용이 동일한가?
# v1 is v2 : 변수 v1과 v2가 참조하는 객체는 동일 객체인가?

r3 = [1, 2, 3]
r4 = r3
if r4 is r3:
    print(True)

r5 = ['John', ('man', 'USA'), [175, 23]]
r6 = list(r5)
if (r6[0] is r5[0]):
    print(True)
if (r6[1] is r5[1]):
    print(True)
if (r6[2] is r5[2]):
    print(True)

# shallow copy, python의 기본 방식.
J2022 = ['John', ('man', 'USA'), [175, 23]]
J2023 = list(J2022)
J2023[2][1] += 1
print(J2023)
print(J2022) # shallow copy로 2022의 나이도 바뀌어버림

import copy

J2023 = copy.deepcopy(J2022)
J2023[2][1] += 1
print(J2022)
print(J2023) # deepcopy로 변경 x

# deep copy는 immutable 은 얕은복사를, mutable은 깊은 복사를 실행함.