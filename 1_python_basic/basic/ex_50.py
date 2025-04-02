import random

class Linear:
    def __init__(self, in_feature, out_feature):
        # 가중치 초기화 (in_feature x out_feature)
        self.weight = [
            [random.random() for _ in range(out_feature)]
            for _ in range(in_feature)
        ]

        # 편향 초기화 (out_feature 크기만큼)
        self.bias = [random.random() for _ in range(out_feature)]

    def matmul(self, A, B):
        # A: m x n, B: n x p → C: m x p
        C = []
        for row in range(len(A)):
            result_row = [0 for _ in range(len(B[0]))]
            C.append(result_row)

        for row in range(len(A)):
            for col in range(len(B[0])):
                for num in range(len(A[0])):
                    C[row][col] += A[row][num] * B[num][col]
        return C

    def forward(self, x):
        # Z = xW + b
        Z = self.matmul(x, self.weight)
        for row in range(len(Z)):
            for col in range(len(self.bias)):
                Z[row][col] += self.bias[col]
        return Z

# 테스트
linear = Linear(4, 3)
x = [
    [1, 2, 3, 1],
    [4, 5, 6, 1],
    [4, 5, 6, 1]
]

print("Weight:")
for i in linear.weight:
    print(i)

print("\nBias:")
print(linear.bias)

print("\nForward Output:")
for i in linear.forward(x):
    print(i)
