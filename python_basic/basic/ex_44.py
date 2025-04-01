operations = {
    '+': lambda x, y: x+y,
    '-': lambda x, y: x-y,
    '*': lambda x, y: x*y,
    '/': lambda x, y: x/y if y != 0 else "오류 0으로 나눌 수 없습니다.",
}

x = float(input("x: "))
y = float(input("y: "))
op = input("연산자(+, -, *, /): ")

if op in operations:
    result = operations[op](x, y)
    print(result)
else:
    print("올바른 연산이 아닙니다.")

# while True:
#     num1 = int(input("첫 번째 숫자를 입력해주세요: "))
#     num2 = int(input("두 번째 숫자를 입력해주세요: "))
#     print("")
#     print("종료하려면 q를 눌러주세요")
#     op = input("연산자를 입력해주세요(+, -, *, /): ")

#     result = 0
#     if op == '+':
#         result = operations[op](num1, num2)
#         print(result)
#     elif op == '-': 
#         result = operations[op](num1, num2)
#         print(result)
#     elif op == '*': 
#         result = operations[op](num1, num2)
#         print(result)
#     elif op == '/': 
#         result = operations[op](num1, num2)
#         print(result)
#     elif op == 'q': 
#         break
#     else:
#         print("연산자를 다시 눌러주세요")
