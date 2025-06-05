student_name = input("너의 이름은: ")
korean_score = int(input("국어 점수는: "))
english_score = int(input("영어 점수는: "))
math_score = int(input("수학 점수는: "))
science_score = int(input("과학 점수는: "))

total_score = korean_score + english_score + math_score + science_score
mean_score = (korean_score + english_score + math_score + science_score) / 4

print(f"{student_name}의 총점은 {total_score}이고 평균은 {mean_score}이다.")