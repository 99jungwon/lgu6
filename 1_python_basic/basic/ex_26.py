while True:
    print("[메뉴를 입력하세요]")
    menu = input("1.게임시작   2.랭킹보기   3.게임종료 >>> ")

    if menu == "1":
        print("-> 게임을 시작합니다.")
    elif menu == "2":
        print("-> 실시간 랭킹")
    else:
        print("게임을 종료합니다.")
        break