def playerAgent(state,piece,ordlist):
    print("Your piece is: %s" % piece)
    coord = getInput()
    return coord

def getInput():
    x,y = (None,None)
    valid = False
    while(not valid):
        while(type(x)!=int):
            try:
                x = int(input("Input X coord: "))
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except:
                print("Numbers please")
                x = None
        while(type(y)!=int):
            try:
                y = int(input("Input Y coord: "))
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except:
                print("Numbers please")
                y = None
        valid = True
        confirm = input("(%d,%d) is your input. Are you sure? Press anything to continue or N to reinput. "%(x,y))
        if confirm == "N" or confirm == "n":
            valid = False
            x = None
            y = None
    return (x,y)

