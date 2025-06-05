operations = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y if y != 0 else "오류 0으로 나눌 수 없습니다.",
}

try:
    x = float(input("x: "))
    y = float(input("y: "))
    op = input("연산자(+, -, *, /): ")
    result = operations[op](x, y)
    print(result)

except ZeroDivisionError as e:
    print("0으로 나눌 수 없음")
    print(e)

except ValueError as e:
    print("입력 값을 확인하세요")
    print(e)

except KeyError as e:
    print("연산자는 +, -, *, / 만 사용")
    print(e)

except Exception as e:
    print("알 수 없는 예외 발생")
    print(e)

finally:
    print("프로그램 종료")