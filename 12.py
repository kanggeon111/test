# 네임드 튜플

# 네임드 튜플의 이해와 작성

from collections import namedtuple  # collections 모듈의 namedtuple 호출

Tri = namedtuple('Triangle', ['bottom', 'height']) # 네임드 튜플 클래스 만듦
t = Tri(3, 7) # 네임드 튜플 객체 생성
print(t[0], t[1])
print(t.bottom, t.height)

Tri = namedtuple('Triangle', ['bottom', 'height']) # 네임드 튜플 클래스 만듦
# 'Triangle'이라는 이름의 클래스 생성, 값의 이름 부여 ( 첫 번째 위치의 이름은 bottom, 두 번째 위치의 이름은 height로 정하겠다.
# t[0] = 15 # 튜플은 값 수정 x

# 네임드 튜플 언패킹
# 튜플과 마찬가지로 네임드 튜플을 대상으로도 다음과 같이 언패킹을 진행할 수 있다.

t = Tri(12, 79)
a, b = t
print(a, b)

# 함수에 값을 전달할 때에도 *을 붙여서 언패킹을 할 수 있다.
def show(n1, n2):
    print(n1, n2)

t = Tri(3, 8)
# show(t)
show(*t)