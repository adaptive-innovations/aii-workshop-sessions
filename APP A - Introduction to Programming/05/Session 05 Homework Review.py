'''
Using a WHILE loop, continue to ask for attendees to attend the party.
If they're already on the list, don't add them. 
If their name can be cast as a number, tell them they have a dumb name.
If the user types in a safe word, the WHILE loop exits. Sort the list.
Finally, use a FOR loop to print the attendees on the list one at a time.
'''

# Another way to check
while True == True:
    conclusion = False
    x = input("Type something in: ")
    try: 
        y = int(x)
        print("That's an int!")
        conclusion = True
    except:
        print("That's NOT an int!")

    if conclusion == True:
        pass #Do things you would do if it was true

# Print List Cursor Position
theList = ["Jeff", "Lewis", "Greg"]
cursor = 0
print(theList[cursor])