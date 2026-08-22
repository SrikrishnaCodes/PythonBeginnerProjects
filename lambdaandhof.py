from functools import reduce
def square(num): return num * num
# square = lambda num : num * num


print(square(3))


def add2(num): return num + 2
# add2 = lambda num : num + 2


print(add2(5))


def sum_total(a, b): return a + b
# sum = lambda a, b : a + b


print(sum_total(23, 28))

###############################


def funcBuilder(x):
    return lambda num: num + x


addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(8))
print(addTwenty(8))

################################

numbers = [5, 9, 14, 18, 27, 32]

squared_nums = map(lambda num: num * num, numbers)

print(list(squared_nums))

################################

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

################################

nums = [1, 2, 3, 4, 5, 3, 3, 2, 3, 4]

total = reduce(lambda acc, curr: acc + curr, nums, 25)
print(total)

print(sum(nums, 25))


names = ['poori jaganath', 'varanasi', 'hyderabad']

length = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(length)
