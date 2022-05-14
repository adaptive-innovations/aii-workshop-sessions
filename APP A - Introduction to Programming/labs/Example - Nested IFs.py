x = input("Which Store do you want to go to? ")

if x == "Vons":
    y = input("What do you have a hankering for? ")
    if y == "Gum":
        print("That's on Aisle 5")
    elif y == "Beer":
        print("That's on Aisle 67")
    else:
        print("I have no idea where that is!")

elif x == "CVS":
    print("You are either an outcast prince with no idea how the real world works, or a pauper with no other choice!")

else:
    print("You have very poor taste, sir!")