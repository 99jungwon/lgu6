radius = float(input("원의 반지름을 입력하세요: "))
pi = 3.14
circle_area = pi * (radius**2)

print(f"반지름이 {radius}인 원의 면적은 {circle_area}")
print(f"이 원의 둘레는 {2*pi*radius}")
print(f"이 원의 지름은 {2*radius}")

# round(변수, 2)
# 이렇게하면 소수점 2번째 자리까지 출력해준다