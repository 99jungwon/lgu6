# 사용자에게 5번의 기회를 주고 패스워드를 입력 받는 로그인 로직

count_id = 0

for i in range(0, 5):
    count_id += 1
    my_id = input(f"({count_id}번째 시도)id를 입력해주세요(5번 기회): ")

    if my_id == "doosan":
        count_pw = 0
        for i in range(0, 5):
            count_pw += 1
            my_password = input(f"({count_pw}번째시도) 비밀번호를 입력해주세요(5번 기회): ")

            if my_password == "20251":
                print("로그인에 성공했습니다.")
                exit()
            else:
                print("비밀번호가 틀렸습니다.")
    else:
        print("id가 잘못 입력되었습니다.")

print("로그인 시도 횟수가 초과했습니다. 프로그램을 종료합니다.")