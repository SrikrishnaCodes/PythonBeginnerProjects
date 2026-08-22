def add1(num):
    if num >= 9:
        return num+1
    total = num + 1
    print(total)
    return add1(total)


newtotal = add1(2)
print(newtotal)
