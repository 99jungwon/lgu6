# *
# **
# ***
# ****
# *****

n = 5
for i in range(n):
    row = ''
    for j in range(i+1):
        row += '*'
    print(row)

for i in range(5): # 줄수
    for j in range(0, i + 1): # *수
        print("*", end='')
    print()

for i in range(0, 5):
    print(f"{'*' * (i + 1)}")