num1 = 12
num2 = 3
if ((num1 < 5) and isinstance(num1, int)): # checks if condition is met
    print("num1 is an integer and is less than 5")
elif(num1 != num2): # checks for another condition, can have mnay else-if
    if(isinstance(num2,int)): # nested if statment
        print("num1 and num2 are not the same but num2 is definety an integer")
else:
    print("no conditions were met")
# when a condition is met the program follows that part of the if statement and
# leaves the if statement when it is done, so the order of else-if statments
# matter
