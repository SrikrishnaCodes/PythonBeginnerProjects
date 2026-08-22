user = {
    "name": "Enderman",
    "height": 200,
    "age": 38,
    "is_admin": True
}

user2 = dict(name="Zombie", height=120, age=24, is_admin=False)

print(user)
print(user2)
print(type(user))
print(type(user2))
print(len(user))
print(len(user2))

# Access items
print(user["name"])
print(user2["name"])
print(user.get("is_admin"))

# list all keys/values
print(user.values())
print(user.keys())

# list of values/keys as tuples
print(user.items())

# verify if key exists
print("age" in user)
print("address" in user)

# changes values
user["age"] = 40
user.update({"weight": 65})
print(user)

# remove items
print(user.pop("weight"))
print(user)
print(user.popitem())  # removes latest addition and returns tuple
print(user)

# delete and clear items
user["age"] = 40
del user["age"]
print(user)

user2.clear()
print(user2)

# copy dictionary

# user2 = user #creates reference and not copy

user2 = user.copy()  # good copy

# or use the dict() counstrustor function

user3 = dict(user)  # copy and not reference

# nested dictrionary
print('')

member1 = {
    'name': 'Rohit',
    'role': 'Manger'
}
member2 = {
    'name': 'Rohan',
    'role': 'SDE'
}
company = {
    'member1': member1,
    'member2': member2,
}
print(company)
print(company["member1"]["role"])


# sets

nums = {1, 2, 3, 4}
nums2 = {0, 1, 2, 3, 4, 5}
print(nums)
print(nums2)
print(type(nums2))
print(len(nums2))

# no duplicates allowed

nums3 = {37, 37, 43, 2, 1}
print(nums3)

# True is duplicate of 1 and False is duplicate of 0
nums4 = {True, 2, 3, 0, False, 1}
print(nums4)
# check if value is in set
print(3 in nums4)
# but we cant reference a value with index or key

# add new element to set
nums.add(24)
print(nums)

# add element from one set to another
morenums = {49, 34, 25, 36}
nums.update(morenums)
print(nums)

# we can use update with lists, tuples and dictionaries

# merge two sets to make new one
one = {1, 2, 3, 4}
two = {0, 5, 6}
newset = one.union(two)
print(newset)

# interserction
one = {1, 2, 3, 4}
two = {0, 5, 6, 4}
one.intersection_update(two)
print(one)

# keep everything but duplicates
one = {1, 2, 3, 4}
two = {0, 5, 6, 4}
one.symmetric_difference_update(two)
print(one)
