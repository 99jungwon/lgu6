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

input_files = os.listdir('./data')

with open('ex_48.txt', 'w') as fw:
    for file in input_files:
        if file[-3:] == 'txt':
            name = file[:-4]
            print(name)

            scores = []
            with open(f"./data/{file}", 'r', encoding='UTF-8') as f:
                lines = f.readlines()
                for line in lines:
                    scores.append(int(line))
                print(scores)
            m = round(ex_45.mean(scores), 2)
            sigma = round(ex_45.std(scores), 2)

            fw.write(f"{name}: {m}, {sigma}\n")
            







