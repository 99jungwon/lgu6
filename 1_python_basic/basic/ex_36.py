A = [[1, 0, 1],
     [0, 2, 0],
     [1, 2, 1]]

B = [[2, 3, 1],
     [0, 1, 1],
     [1, 1, 1]]

C = []  # 빈 리스트 생성

for _ in range(len(A)):  # A의 행 개수만큼 반복
    row = []  # 새로운 행(리스트) 생성
    for _ in range(len(A[0])):  # A의 열 개수만큼 반복
        row.append(0)  # 각 열에 0을 추가
    C.append(row)  # 완성된 행을 C에 추가

print(C)

for row in range(len(A)): # 0 1 2
    for col in range(len(A[0])): # 0 1 2
        for num in range(len(A[0])): # 0 1 2
            C[row][col] += (A[row][num] * B[num][col])

print(C)

# a = [1, 2, 3, 4]
# b = [4, 5, 6, 7]
# c = [0, 0, 0, 0]
# for i in range(len(a)):
#     c[i] = a[i] * b[i]

# print(c)