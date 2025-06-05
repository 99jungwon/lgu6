import random

class Digit3:
    def __init__(self):
        self.player_list = {}
        self.cur_player = None

    def init_game(self):
        ############################################################
        # 3자리 숫자 초기화
        # 각자리가 중복되면 안되고
        # 첫자리가 0이 되면 안되고
        # hint: 문자로 한 자리씩 숫자를 생성해서 0인지 검사하고 
        #       앞 숫자와 겹치는지 검사
        self.d = []

        ############################################################
        # 위에서 초기화된 맞혀야 하는 숫자
        self.d.append(random.randint(1,9)) # 첫번째 숫자
        while len(self.d) < 3:
            num = random.randint(0,9) # 두, 세번째 숫자
            if num not in self.d:
                self.d.append(num)

        # 개발 과정에서 내부적으로 초기화한 숫자를 화면에 뿌림
        # print('init_game:', self.d)


    def q(self, digit):
        # digit: 사용자로부터 입력된 세자리수
        # digit이 self.d와 일치하는지 검사해서
        # 볼카운트를 다음과 같은 사전으로 만들어 반환
        # {'ball': 2, 'strike': 1}

        strike  = 0
        ball = 0

        ############################################################
        # self.d와 digit을 비교하여 볼카운트를 생성
        # hint: 숫자를 문자로 다루기..."123"
        #       str.count()함수 사용
        for i in range(3):
            num = int(digit[i])
            if num == self.d[i]: # 같은 자리에 있을때 스트라이크 + 1
                strike += 1
            elif num in self.d: # 같은 자리는 아니지만 self.d에 있을때 볼 + 1
                ball += 1
        ############################################################

        # 볼카운트가 저장된 변수를 리턴
        return {'ball': ball, 'strike': strike}
    
    def rank(self):
        # 현재 self.player_list에 저장된 플레이어들의 성적을 출력
        # 플레이어 "아이디 {점수}회 만에 성공" 형식으로 출력
        # self.payer_list 형식
        # {'플레이어1': 점수, '플레이어2': 점수}
        # hint: sorted()함수 사용, 정렬 키는 lambda식 사용
        sorted_players = sorted(self.player_list.items(), key=lambda item: item[1])

        for player, score in sorted_players:
            print(f"{player}: {score}")

    def set_player(self):
        self.cur_player = input("플레이어 아이디를 입력하세요: ")

        if self.cur_player not in self.player_list:
            print('신규 플레이어 초기화')
            self.player_list[self.cur_player] = 0
        else:
            print(f"{self.cur_player}님의 현재 최고 기록: {self.player_list[self.cur_player]}회")


    def start_game(self):
        # 게임을 초기화 
        self.init_game()

        # 플레이어 세팅
        self.set_player()
        
        count = 0

        # 게임 루프
        # 게임이 끝날 때 까지 무한 반복
        # 루프 중 고려해야할 사항
        # 1. 사용자 입력 유효성 검사, 3자리 숫자인지, 숫자인지
        # 2. 플레이어가 정답을 맞히면 self.palyer_list에 점수를 저장하고 루프를 탈출
        #    점수를 저장할 때 기존 점수보다 더 좋은 점수일 경우에만 저장
        while True:
            digit = input("숫자를 입력해주세요: ")

            if len(digit) != 3:
                print("3자리 숫자를 입력해주세요.")
            elif digit.isdigit() == False:
                print("숫자만 입력해주세요.")
            else:
                count += 1
                result = self.q(digit)
                print(f"{result['strike']} Strike, {result['ball']} Ball")

                if result['strike'] == 3:
                    print(f"{count}번 만에 맞았습니다!")
                    prev_score = self.player_list[self.cur_player]
                
                    # 기존 점수가 없거나 더 좋은 기록이면 갱신
                    if prev_score == 0 or count < prev_score:
                        self.player_list[self.cur_player] = count

                    break
    

if __name__ == '__main__':
    for i in range(2):
        # 게임 객체를 생성
        digit3 = Digit3()
        digit3.start_game()
        # 플레이어의 성적을 화면에 뿌림
        digit3.rank()



