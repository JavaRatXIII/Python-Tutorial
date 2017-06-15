list1 = [23,2,4,8,"ten"]
count = 0
while count < len(list1): # print each item of list1
    print(list1[count])
    count = count + 1 # by incrementing a counter

print("\n")
count2 = 0
count = 0
while count < len(list1):
    while count2 < len(list1):
        count2 = count2 + 1
        print(list1[count])
    count = count + 1
    count2 = 0
# 2 while loops nested in, so each item gets printed out for the length of the
# list so each item prints 5 times
