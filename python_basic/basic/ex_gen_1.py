
def get_number_generator(n):
    for i in range(n):
        print("before yield")
        yield i
        print("after yield")

number = get_number_generator(3)

print(next(number, 'end'))
print()

print(next(number, 'end'))
print()

print(next(number, 'end'))
print()