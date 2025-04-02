
def get_number_generator(n):
    while True:
        for i in range(n):
            print("before yield")
            yield i # 값을 반환하고 실행을 멈춤
            print("after yield")