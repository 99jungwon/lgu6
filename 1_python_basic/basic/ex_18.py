# 사용자로부터 숫자를 입력 받고
# 그 숫자가 0이 될 때 까지 while루프를 반복하고
# 반복 번수를 출력

num = int(input("숫자를 입력해주세요: "))
count = 0

while num > 0:
    num -= 1
    count += 1

print(f"최종 숫자는 {num}, 반복 번수는 {count}입니다.")