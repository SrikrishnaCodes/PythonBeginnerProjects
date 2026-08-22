x = 2


class JustNotCoolError(Exception):
    pass


try:
    raise JustNotCoolError("It's just not cool man!")
    # print(x/1)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed!")
    # raise Exception("I'm a custom exception.")

except ZeroDivisionError:
    print("Please do not divide by zero.")
except NameError:
    print("NameError means some variable is not defined.")
except Exception as error:
    print(error)
else:
    print("There are no errors!")
finally:
    print("I'm going to print with or without an error.")
