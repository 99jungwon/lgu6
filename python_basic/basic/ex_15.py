import math

pi = 3.14
e = 2.72
x = float(input("a: "))
mu = float(input("mu: "))
sigma = float(input("sigma: "))

num =  1 / (sigma * math.sqrt(2 * pi)) * (e ** -(((x - mu) ** 2) / (2 * (sigma **2))))
print(f"{num}")
