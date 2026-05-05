# def my_generator():
#     for i in range(50000000):
#         yield i

# gen = my_generator()
# print(next(gen))
# print(next(gen))

def countdown(start):
    while start > 0:
        yield start
        start -= 1

for num in countdown(5):
    print(num)
