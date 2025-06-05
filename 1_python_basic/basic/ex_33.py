# jisoo = [90, 85, 93]
# mansoo = [78, 92, 89]

# 지수, 만수의 점수
# jisoo = []
# jisoo_total = 0
# mansoo = []
# mansoo_total = 0

# for i in range(len(scores)):
#     for j in range(len(scores[0])):
#             if i == 0:
#                 jisoo.append(scores[i][j])
#                 jisoo_total += jisoo[j]
#             else:
#                  mansoo.append(scores[i][j])
#                  mansoo_total += mansoo[j]

scores = [[90, 85, 93], 
          [78, 92, 89]]

# 쌤 코드(학생 개인의 총합 점수)
total_by_students = []

# st : 0, 1
for st in range(len(scores)):
    total = 0
    for sb in range(len(scores[0])):
       total += scores[st][sb]
    total_by_students.append(total)

print(total_by_students)

# sb = 0, 1, 2(과목별 점수)
total_by_subjects = []
# sb : 0, 1, 2 st = 0, 1
for sb in range(len(scores[0])):
    total = 0
    for st in range(len(scores)):
        total += scores[st][sb]

    total_by_subjects.append(total)

print(total_by_subjects)

scores = [[90, 85, 93], 
          [78, 92, 89]]

# 한번에 둘다 해버림
total_by_students = [0] * len(scores)
total_by_subjects = [0] * len(scores[0])

for st in range(len(scores)):
    for sb in range(len(scores[0])):
        total_by_students[st] += scores[st][sb]
        total_by_subjects[sb] += scores[st][sb]

print(total_by_students)
print(total_by_subjects)


# column_sums = [0] * len(scores[0])
# print(column_sums)

# for i in range(len(scores)):        
#     for j in range(len(scores[0])): 
#         column_sums[j] += scores[i][j]

# print(column_sums)


# total_score = [jisoo[0] + mansoo[0], jisoo[1] + mansoo[1],
#                jisoo[2] + mansoo[2]]
# print(total_score)

# total_score = []

# for i in range(len(jisoo)):
#     total_score.append(jisoo[i] + mansoo[i])

# print(total_score)




