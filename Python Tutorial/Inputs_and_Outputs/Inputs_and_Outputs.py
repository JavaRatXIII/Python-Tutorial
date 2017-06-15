input1 = input("would you like to have a conversation (yes) (no) ")
if(input1=="yes"):
    print("Really! Thanks.")
    print("..... I guess I didn't really have anything say")
    print("Sorry. Bye")
else:
    print("Oh um okay, then")

inputnum = int(input("Give me a number before we leave ")) # int converts string
                                                           # into an integer
if(inputnum < 10):
    print("That's low")
else:
    print("Okay thanks")
