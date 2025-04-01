numbers = [-10, -4, -5, -1, -6, -12, -40]

max = numbers[0]
for i in numbers:
    if max < i:
        max = i
print(max)


# total = 0
# nums = []
# for i in range(len(numbers)):
#     if i % 2 != 0:
#         nums.append(numbers[i])
#         total += numbers[i]

# print(nums)
# print(total)