# dict의 루핑 기술과 컴프리헨션

# 딕셔너리 루핑 테크닉

# 딕셔너리를 대상으로 하는 가장 보편적인 for loop
d = dict(a = 1, b = 2, c = 3)
for k in d:
    print(d[k], end = '\n')
    
# dict.keys() : 딕셔너리의 키들만 참조하고자 할 때
# dict.values() : 딕셔너리의 값들만 참조하고자 할 때
# dict.items() : 딕셔너리의 키와 값을 튜플 형태로 참조하고자 할 때

d = dict(a = 1, b = 2, c = 3)
for k in d.keys():
    print(k, end='\n')

for j in d.values():
    print(j)

for i in d.items(): # item = key, value 순서대로 출력.
    print(i)

for a, b in d.items():
    print(a, b)

d = dict(a = 1, b= 2, c = 3)
vo = d.items()
for kv in vo:
    print(kv)
d['a'] += 3
d['c'] -= 2
for kv in vo:
    print(kv)

# dict comprehension
d1 = dict(a = 1, b = 2, c = 3)
d2 = {k : v*2 for k,v in d1.items()}
print(d2)
d3 = {k : v*2 for k, v in d2.items()}
print(d3)

ks = ['a', 'b', 'c', 'd', 'e']
vs =[1, 2, 3, 4, 5]
d = {k: v for k, v in zip(ks, vs)}
print(d)