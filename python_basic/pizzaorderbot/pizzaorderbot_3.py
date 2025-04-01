def main():
    print("빅데이터 피자 가게에 오신것을 환영합니다.\n")

    menus = {
        '피자': ['페퍼로니 피자', '스테이크 피자', '시푸드 피자'],
        '토핑': ['햄', '페퍼로니', '트러플', '올리브', '새우'],
        '사이드': ['치즈 오븐 스파게티', '리조또', '치킨 윙'],
        '음료': ['콜라', '스프라이트', '오렌지 쥬스']
    }
    prices = {
        '피자': [29000, 32000, 32000],
        '토핑': [500, 500, 800, 300, 800],
        '사이드': [9900, 8900, 8900],
        '음료': [1000, 1000, 1000]

    }
    orders = {'피자': [], '토핑': [], '사이드': [], '음료': []}

    categories = ['피자', '토핑', '사이드', '음료']
    i = 0
    
    while True:
        current_category = categories[i]
        print(f"{current_category}를 선택하세요. 수량 추가를 위해 여러 번 선택 가능합니다.")

        print(f"현재 장바구니: '피자': [{orders['피자']}], '토핑': [{orders['토핑']}], '사이드': [{orders['사이드']}], '음료': [{orders['음료']}]")
        for idx, item in enumerate(menus[current_category]): 
            print(f"{idx + 1}. {item} ({prices[current_category][idx]}원)")
        
        choice = input("번호를 입력하고 Enter를 누르세요.(다음단계:n, 이전단계:p, 주문완료: f): ")

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(menus[current_category]):
                print(f"선택된 메뉴: {menus[current_category][choice-1]}\n")
                orders[current_category].append(menus[current_category][choice - 1])
            else:
                print("없는 메뉴 번호입니다. 다시 입력해주세요.\n")
        else:
            if choice == "f":
                print("----------")
                print("주문   내역")
                print("----------")
                
                total = 0
                for k, v in orders.items():
                    for idx in v:
                        total += prices[k][menus[k].index(idx)]
                    print(f"{k}: {','.join(v)}")
                print(total)
                print("주문이 완료되었습니다. 감사합니다\n")
                
                break

            elif choice == "n":
                if i < len(categories) - 1:
                    i += 1
                    print(f"다음: {categories[i]}")
                else:
                    print("이미 마지막 카테고리입니다.")

            elif choice == "p":
                if i > 0:
                    i -= 1
                    print(f"이전: {categories[i]}")
                else:
                    print("이미 첫 번째 카테고리입니다.")
            else:
                print("S잘못된 입력입니다.")
    
main()