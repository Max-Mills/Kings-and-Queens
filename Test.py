

### Gives a number for the royal cards ###
def royals(test):

    num = 0

    try:
        num = int(test)
    except ValueError:
        if test == "Jack":
            num = 11
        elif test == "Queen":
            num = 12
        elif test == "King":
            num = 13
        elif test == "Ace":
            num = 14
        else:
            pass
    return num

### Checks to see if a number or royality was given, if not repeat the question ###
def checkiscard(question):

    while True:
        tester = input(question)
        print()
        if tester in ("Jack", "Queen", "King", "Ace", "pass"):
            return tester
        try:
            test = int(tester)
        except ValueError:
            print("That was not a number")
        else:
            return test