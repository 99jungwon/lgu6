#     *     4공백 1*
#    ***    3공백 3*
#   *****   2공백 5*
#  *******  1공백 7*
# ********* 0공백 9*


for i in range(5):    # 0 1 2 3 4
    for j in range(5 - i - 1): # 4 3 2 1 0
        print(' ', end='')
    for k in range((i * 2) + 1): # 1 3 5 7 9
        print('*', end = '')
    print()

for i in range(5):
    print(' ' * (5-i-1) + '*' * (i*2+1))