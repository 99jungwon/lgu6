import random

lottery = []

while len(lottery) < 6:
    n = random.randrange(1, 47)
    if len(lottery) == 0:
        lottery.append(n)
    else:
        if n not in lottery:
            lottery.append(n)
        


print(lottery)

