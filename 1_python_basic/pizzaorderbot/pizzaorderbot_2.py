def main():
    print("빅데이터 피자 가게에 오신것을 환영합니다.\n")

    menus = {
        '피자': ['페퍼로니 피자', '스테이크 피자', '시푸드 피자'],
        '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우']
    }
    prices = {
        '피자': [29000, 32000, 32000],
        '토핑': [500, 500, 800, 300, 800]
    }
    order = {'피자': [], '토핑': []}

    categories = ['피자', '토핑']
    i = 0
    current_category = categories[i]
    
    while True:
        for i in categories:
            print(f"{i}를 선택하세요. 수량 추가를 위해 여러 번 선택 가능합니다.")
            for idx, item in enumerate(menus[i]): 
                print(f"{idx + 1}. {item} ({prices[i][idx]}원)")
            
            choice = input("번호를 입력하고 Enter를 누르세요.(주문완료는 f를 누르세요): ")

            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(menus[i]):
                    print(f"선택된 메뉴: {menus[i][choice-1]}\n")
                    order[i].append(menus[i][choice - 1])
                else:
                    print("없는 메뉴 번호입니다. 다시 입력해주세요.\n")
            else:
                if choice == "f":
                    print(order)
                    exit()
                else:
                    print("메뉴를 제대로 선택해 주세요")
    
main()