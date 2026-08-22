person = "Creeper"
coins = 5

print("\n" + person + " has " + str(coins) + " coins left.")

message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person)
print(message)

player = {'person': 'Creeper', 'coins': '5'}

message = "\n{person} has {coins} coins left.".format(**player)
print(message)


# f-strings

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {2*5} coins left."
print(message)

message = f"\n{person.lower()} has {2*5} coins left."
print(message)

message = f"\n{player['person']} has {player['coins']} coins left."
print(message)

# we can pass formatting optioms
num = 10
print(f'\n2.25 times {num} is {2.25 * num:.2f}')  # second f is fixed

for num in range(1, 11):
    print(f'2.25 times {num} is {2.25 * num:.2f}')

for num in range(1, 11):
    print(f'{num} divided by 3.68 is {num / 3.68:.2%}')
