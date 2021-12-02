while 1==1:
    x = input("Enter a number: ")
    try:
        y = int(x)
    except Exception as myErrorVariable:
        print(myErrorVariable)