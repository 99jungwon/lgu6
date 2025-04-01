def score_mean(l):
    total = sum(l)
    mean = total / len(l)
    return mean


X = [[78, 80, 95, 55, 67, 43], [45, 67, 90, 87, 88, 93]]

mean_score = [round(score_mean(i), 2) for i in X]
print(mean_score)

########################################################
# 기본 인자
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

greet('홍길동')
