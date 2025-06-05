# 구구단

num = int(input("출력하고 싶은 단수를 입력해주세요: "))

for i in range(1, 10):
    print(f"{num} X {i} = {num * i}")