def main():
    print("빅데이터 피자 가게에 오신것을 환영합니다.\n")

    menus = ['페퍼로니 피자', '스테이크 피자', '시푸드 피자']
    price = [29000, 32000, 32000]
    order = []


    while True:
        print("피자를 선택하세요. 수량 추가를 위해 여러 번 선택 가능합니다.")
        for idx, item in enumerate(menus): 
            print(f"{idx + 1}. {item} ({price[idx]}원)")

        choice = input("번호를 입력하고 Enter를 누르세요.(주문완료는 f를 누르세요): ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(menus):
                print(f"선택된 메뉴: {menus[choice-1]}")
                order.append(menus[choice - 1])
            else:
                print("없는 메뉴 번호입니다. 다시 입력해주세요.\n")
        else:
            if choice == "f":
                print(order)
                break
            else:
                print("메뉴를 제대로 선택해 주세요")
    
main()