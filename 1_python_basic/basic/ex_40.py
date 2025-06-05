def Qr():
    while True:
        num1 = int(input("나눠질 수를 입력하세요: "))
        num2 = int(input("나눌 수를 입력하세요: "))

        if num1 > 0 and num2 > 0:
            q = 0
            while num1 >= num2:
                num1 -= num2
                q += 1
                
            r = num1

            return (q, r)
        else:
            print("양수를 입력하세요.")

print(Qr())
