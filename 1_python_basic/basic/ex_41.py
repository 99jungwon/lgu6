# 숫자로 채워진 리스트 또는 튜플을 입력 받아 평균을 구하는 함수

a = [1, 4, 5, 10, 24, 2, 5, 3]

def mean(l):
    total = sum(l)
    mean = total / len(l)
    return mean

print(mean(a))