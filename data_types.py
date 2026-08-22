import math
# string data types

# Literal Assignment
first = 'Srikrishna'
last = 'Papolu'
# print(type(first))   prints what class the thing specified is
# print(type(first) == str)   checks if varible is string
# print(isinstance(first, str))   checks if varible is string


# Constructor Function
# pizza = str('Panner')
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


# Concatenation (mixing strings to make big string)(both "" and '' can be used for strings)
# fullname = first + " " + last
# print(fullname)

# fullname += "!"
# print(fullname)


# Casting a number to a string
# year = str('2030')
# print(type(year))
# print(year)

# statement = 'I like music from ' + year + 's.'
# print(statement)


# Multiple lines
# multiline = '''
# Hey wazzup, How are u?

# Just checking in.
#                               all good?.
# '''
# print(multiline)


# Escaping special charachters (\for escaping, \t for tab(smallgap), \n for new line)
# sentance = 'I\'m at work.\tHey!\n\nWhere is this at\\located?'
# print(sentance)


# String Methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace('good', 'ok'))
# print(multiline)

# multiline += '                              '
# multiline = '           ' + multiline
# print(len(multiline))
# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))


# Build a menu
# title = "menu".upper()
# print("Sk\'s Cofee Shop".center(30))
# print(title.center(30, "="))
# print("Coffee".ljust(25, ".") + "10₹".rjust(5))
# print("Tea".ljust(25, ".") + "15₹".rjust(5))
# print("Cake".ljust(25, ".") + "30₹".rjust(5))
# print("Biscuit".ljust(25, ".") + "5₹".rjust(5))
# print("=".center(30, "="))


# String index value
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])


# Some methods return boolean values
# print(first.startswith("S"))
# print(first.endswith("a"))


# boolean data
# myvalue = True
# x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))


# numeric data types
# 1.integer type
# price = 250
# best_price = int(100)
# print(type(price))
# print(isinstance(best_price, int))

# 2.float type
# gpa = 9.865
# y = float(9.72)
# print(type(gpa))

# 3.Complex type
# comp_value = 4+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)


# built-in functions for numbers
# print(abs(gpa))
# print(abs(gpa*-1))
# print(round(gpa))
# print(round(gpa, 1))
# print(round(gpa, 2))

# print(math.pi)
# print(math.sqrt(81))
# print(math.floor(gpa))
# print(math.ceil(gpa))


# Casting a string to a number
# zipcode = "500062"
# zip_value = int(zipcode)
# print(type(zip_value))


# error when incorect data casted
# zip_value = int("zipcode")
