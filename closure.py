# closure is a fuction which has access to its parent function's scope even after parent function has returned

def parent_function(person, coins):
    # coins=4

    def play_game():
        nonlocal coins
        coins -= 1
        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coin left.")
        else:
            print("\n" + person + " has no coins left.")

    return play_game


Creeper = parent_function("Creeper", 5)
Skeleton = parent_function("Skeleton", 2)

Creeper()
Creeper()
Skeleton()
Creeper()
Creeper()
Skeleton()
