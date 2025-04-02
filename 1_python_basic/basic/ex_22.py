# 사용자에게 임의의 자연수 n을 입력받고 1에서 n까지 모두 합산하는 프로그램

num = int(input("임의의 자연수 n을 입력해주세요: "))
result = 0

for i in range(1, num + 1 ):
    result += i

print(f"1부터 num까지의 합은 {result}입니다.")