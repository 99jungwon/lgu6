# bmi < 18.5 저체중
# 18.5 <= bmi < 23 정상
# 23 <= bmi < 25 과체중
# 25 <= bmi 비만

# bmi = float(input())

height = float(input("키를 입력해주세요: "))
weight = float(input("몸무게를 입력해주세요: "))

bmi =  weight / (height**2)

if bmi < 18.5:
    print("저체중")
elif bmi < 23.5:
    print("정상")
elif bmi < 25:
    print("과체중")
else:
    print("비만")

