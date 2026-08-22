value = 1

# while value <= 10:
#     print(value)
#     if value == 7:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 7:
#         continue
#     print(value)
# else:
#     print("Value is " + str(value))


names = ["Zombie", "Creeper", "Skeleton"]

# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Creeper":
#         break
#     print(x)

# for x in names:
#     if x == "Creeper":
#         continue
#     print(x)

# for x in range(5):
#     print(x)

# for x in range(2, 5):
#     print(x)

# for x in range(0, 101, 20):
#     print(x)
# else:
#     print("Very few numbers!")

names = ["Zombie", "Creeper", "Skeleton"]
actions = ["Shoots", "Bites", "Hisses"]

# for name in names:
#     for action in actions:
#         print(name + ' ' + action + '.')

for action in actions:
    for name in names:
        print(name + ' ' + action + '.')
