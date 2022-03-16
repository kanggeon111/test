# 05.py Iterable & Iterator

# iter 함수

ds = [1, 2, 3, 4]
for i in ds:
    print(i, end = " ")

ir = iter(ds) # iterator 객체를 얻는 법
print(next(ir)) # 다음 값을 반환해라!
print(next(ir))
print(next(ir))
print(next(ir))
# print(next(ir))  # 마지막 값까지 얻었으면 StopIteration 예외 발생
ir = iter(ds)
next(ir)

# Iterable 객체 : iter 함수에 인자로 전달 가능한 객체
# Iterator 객체 : iter 함수가 생성해서 반환하는 객체 ex) list

# iterable 객체를 대상으로 iter 함수를 호출해서 iterator 객체를 만든다.

ds = [5, 6, 7, 8]
ir = ds.__iter__() # iter함수의 실제 호출 모습
print(ir.__next__()) # next함수의 실제 호출 모습

# 리스트의 __iter__ 메소드 호출을 통해서 iterator 객체를 얻게 된다.
# iterator 객체의 __next__ 메소드 호출을 통해서 값을 하나씩 얻게 된다. => 스페셜 메소드

# 객체 생성 시 자동으로 호출되는 __init__메소드도 스페셜 메소드.
# 스페셜 메소드 => 앞뒤로 __fmf qnxduwnsek.

#Iterable 객체의 종류와 확인 방법
# tuple
td = ('one', 'two', 'three')
ir = iter(td)
print(next(ir))
print(next(ir))
print(next(ir))

# 문자열
s = 'iteration'
ir = iter(s)
print(next(ir))
print(next(ir))
print(next(ir))
print(next(ir))

print(dir([1, 2]))

# 실제 동작

for i in [1, 2, 3]:
    print(i, end = ' ')

ir = iter([1, 2, 3])
while True:
    try:
        i = next(ir)
        print(i, end = ' ')
    except StopIteration:
        break

# 따라서 for 루프는 iterable 객체여야 한다.