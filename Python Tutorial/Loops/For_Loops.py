print("Print each letter in the string 'Today is a nice day'")
for letter in "Today is a nice day":
    print(letter)

list1 = [12,23,"twelve",2.99,"brother","sister"] # list noted by square brackets
string1 = ""
for item in list1:
    if(item == 23):
        continue # continue to skip 23
    elif(item == "brother"):
        break # break out of loop if item is brother
    string1 = string1,item # add each item of list1 to string1

print(string1)
