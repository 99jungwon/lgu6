# with open("file_w.txt", "w", encoding = "utf-8") as f:
#     f.write("Hello\n")
#     f.write("안녕안녕")

# with open("file_w.txt", "r", encoding = "utf-8") as f:
#     lines = f.readlines()
#     # print(lines, type(lines))
#     for line in lines:
#         print(line, end='')

import ex_45
import os

# file_name = os.listdir('./data')
# print(file_name)

# txt_file = [file for file in file_name if file[-4:] == ".txt"]
# print(txt_file)

# data = []
# for score in txt_file:
#     with open(f"./data/{score}", "r", encoding = "utf-8") as f:
#         lines = f.readlines()
#         data.append(lines)

# print(data)

# student_scores = []

# for name, st in zip(txt_file, data):
#     score = []
#     for sc in st:
#         score.append(int(sc[:-1]))
#     mean = ex_45.mean(score)
#     std = ex_45.std(score)
#     student_scores.append([name[:-4], round(mean,2), round(std,2)])

# print(student_scores)

input_files = os.listdir('./data')

with open('ex_48.txt', 'w') as fw:
    for file in input_files:
        if file[-3:] == 'txt':
            print(file)
            name = file[:-4]
            scores = []
            with open(f"./data/{file}", 'r', encoding='UTF-8') as f:
                lines = f.readlines()
                for line in lines:
                    scores.append(int(line))
                print(scores)
            m = round(ex_45.mean(scores), 2)
            sigma = round(ex_45.std(scores), 2)

            fw.write(f"{name}: {m}, {sigma}\n")
            







