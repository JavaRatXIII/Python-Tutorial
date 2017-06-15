def reversecount(num): # def defines a function
    print(num)
    if(num > 0):
        num = num - 1
        reversecount(num) # when a method calls itself it is doing recursion
    elif(num < 0):
        num = num + 1
        reversecount(num) # reccursion
    else:
        return

number = 12
reversecount(number) # method call on the value number
