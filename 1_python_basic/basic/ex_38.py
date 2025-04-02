data = [
    {'name':'철수', 'math':85, 'eng':90, 'sci':75},
    {'name':'준호', 'math':73, 'eng':85, 'sci':93},
    {'name':'영희', 'math':92, 'eng':88, 'sci':90}
]

# {'철수' = [총점, 평균]} 형식
score_data = {}

# for i in data:
#     name = ''
#     total_score = 0
#     mean = 0
#     for k, v in i.items():
#         if type(v) == str:
#             name = v
#         else:
#             total_score += v
#     mean = total_score / (len(data[0]) - 1)
#     score_data[name] = [total_score, mean]

score_data = {}

for d in data:
    name = d['name']
    total_score = 0
    mean = 0
    for k, v in d.items():
        if type(v) == int:
            total_score += v
    mean = total_score / (len(d) - 1)

    score_data[name] = [total_score, round(mean,2)]

print(score_data)



        