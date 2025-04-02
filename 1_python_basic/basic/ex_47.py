import pandas as pd

df = pd.read_excel("./data/scores.xlsx")

df = df.T.to_dict()
data = [v for k, v in df.items()]
print(data)

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