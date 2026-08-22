users = ["Steve", "Baconhair", "Noob"]
data = ["Steve", 37, True]
emptylist = []

print("steve" in data)
print("Steve" in data)

print(users.index('Noob'))

print(users[1])
print(users[0:2])
print(users[-3:-1])
print(users[1:-1])
print(users[1:])

users.append('Enderman')
print(users)
print(len(data))

users += ["Creeper"]
print(users)

users.extend(["Sheep", "Cow"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'EnderDroagon')
print(users)


# users[2:3] = ['Warden', 'Axolotl']  # replaces baconhair
# print(users)
# doesnt replace baconhair
users[2:2] = ['Warden', 'Axolotl', 'Tiaga Villager']
print(users)
users[2:4] = ['skeleton', 'zombie']  # replaces 2 items
print(users)

users.remove('Noob')
print(users)

print(users.pop())  # removes last item
print(users)

del users[6]  # removes item at specified index
print(users)

# del data # removes entire list and gives error
# print(data)

data.clear()  # removes all items but dosent delete list
print(data)

users.sort()
print(users)  # alphabetical arrangement (Capital > Lowercase)

users.sort(key=str.lower)  # ignores case
print(users)

num = [37, 62, 24, 2, 1, 13]
num.reverse()
print(num)

# num.sort(reverse=True) #desending order
# print(num)

print(sorted(num, reverse=True))  # only sorts temporarily
print(num)

numcopy = num.copy()  # all 3 are copy of num
mynum = list(num)
mycopy = num[:]

print(numcopy)
print(mynum)
mycopy.sort()  # dosent change orignial num
print(mycopy)
print(num)

print(type(num))

mylist = list([1, 'bak', False])
print(mylist)


# Tuples (cant be changed and saty in fixed order but can be copied)

mytuple = tuple(('bak', 23, True))
anothertuple = (6, 35, 5, 45, 5, 5)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Skeleton')
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)  # unpacking tuple
print(two)
print(hey)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(5))
