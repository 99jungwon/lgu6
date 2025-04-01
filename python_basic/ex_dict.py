d = {}

d = {
    'foo' : 'foo@naver.com',
    'bar' : 'bar@gmail.com',
    'egg' : 'egg@kakao.com'
}

print(d)

# d[0]
print(d['foo'])

# 값 삭제
del d['foo']
print(d)

# 새로운 값 추가
d['foo'] = 'foo@naver.com'
print(d)

# 기존값 업데이트
d['foo'] = 'foo@gmail.com'

#
d['list'] = [1, 2, 3, 4, 5]
print(d)

print(d.keys())
for key in d:
    print(d[key])

print(d.values())
for value in d:
    print(value)

