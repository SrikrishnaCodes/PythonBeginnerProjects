# def hello():
#     print("Hello lil bro!")

# hello()


def sum(num1=0, num2=0):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


total = sum()
print(total)


def multipleitems(*args):
    print(args)
    print(type(args))


multipleitems("zombie", "creeper", "skeleton")


def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_named_items(first='srikrishna', last='papolu')
