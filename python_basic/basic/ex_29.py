# *****
# ****
# ***
# **
# *

for i in range(5): # 줄수
    for j in range(5-i): # *수
        print("*", end='')
    print()

for i in range(5, 0, -1):
    print(f"{'*' * (i)}")

