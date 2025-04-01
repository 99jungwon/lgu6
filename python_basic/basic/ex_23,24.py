# 아이디를 입력 받고 입력한 아이디가 맞으면 비번 입력받음
# 입력 받은 아이디가 틀리면 그런 아이디는 존재하지 않습니다.

while True:
    id = input("ID를 입력해주세요: ")
    if id == 'python':  # 아이디가 맞으면 비밀번호 입력 단계로 이동
        while True:
            password = input("Password를 입력해주세요: ")
            if password == 'abcd':
                print("로그인이 성공했습니다.")
                break  # 내부 비밀번호 루프 종료
            else:
                print("비밀번호가 틀렸습니다. 다시 입력해주세요.")
        break  # 최종 루프 종료
    else:
        print("아이디가 틀렸습니다. 다시 입력해주세요.")