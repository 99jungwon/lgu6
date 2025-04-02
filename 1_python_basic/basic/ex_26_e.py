from baseball import Digit3

def main():
    game = Digit3()  # Digit3 객체를 한 번만 생성해서 랭킹이 유지되도록

    while True:
        print("[메뉴를 입력하세요]")
        menu = input("1.게임시작   2.랭킹보기   3.게임종료 >>> ")

        if menu == "1":
            print("-> 게임을 시작합니다.")
            game.start_game()  # 게임 시작
        elif menu == "2":
            print("-> 실시간 랭킹")
            game.rank()  # 랭킹 출력
        elif menu == "3":
            print("게임을 종료합니다.")
            break
        else:
            print("올바른 번호를 입력하세요.")

main()
