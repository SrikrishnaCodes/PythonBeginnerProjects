import os

# R = read
# A = append
# W = write
# X = create


# read - error if it dosent exist


file = open("names.txt")

# print(file.read())
# print(file.read(10))
# print(file.read(4))

# print(file.readline())
# print(file.readline())

for x in file:
    print(x)

file.close()

try:
    file = open("name_list.txt")
    print(file.read())
except:
    print("The file u are trying to read dosent exist!\n")
finally:
    file.close()


# Append - creates file if it dosent exist


file = open("names.txt", "a")
file.write("Sumit\n")
file.close()

file = open("names.txt")
print(file.read())
file.close()


# write - overwrite


file = open("context.txt", "w")
file.write("I deleted everything in this file!")
file.close()

file = open("context.txt")
print(file.read())
file.close()


# x(create) - Two ways to create new file

# opens the file for writing and creates the file if it dosent exist

file = open("names_list.txt", "w")
file.close()

# creates specified file, but returns error if file exists
if not os.path.exists("sak.txt"):
    file = open("sak.txt", "x")
    file.close()

# Delete a file

# we can avoid a error if it dosent exist
if os.path.exists("sak.txt"):
    os.remove("sak.txt")
else:
    print("The file u wish to delete does not exist")


with open("more_names.txt") as file:
    content = file.read()

with open("names.txt", "w") as file:
    file.write(content)
