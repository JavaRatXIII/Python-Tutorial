list1 = ['hello', 192, 27.6, 192, 'hi'] # lists are noted with square brackets
count = 0
while(count < len(list1)): # len returns the length of the list
    print(list1[count])
    count = count + 1

print("\n192 appears in list1", list1.count(192), "times")

list1.append("new item")
list1.remove('hello')
count = 0
print("\nnew item has been added to the list while hello was removed")
while(count < len(list1)):
    print(list1[count])
    count = count + 1

list1.reverse()
count = 0
print("\nreverse list1")
while(count < len(list1)):
    print(list1[count])
    count = count + 1

list2 = [12, 6, 21, 3, 1, 54]
print("\nMaximum value of list2 is", max(list2), "minimum value is", min(list2))
list2.sort()
count = 0
print("\nsort list2")
while(count < len(list2)):
    print(list2[count])
    count = count + 1

tuple1 = (23, 'word', 1, 23, 87.3) # tuples are noted by normal brackets
list3 = list(tuple1) # turns tuple1 into a list
count = 0
print("\nlist3")
while(count < len(list3)):
    print(list3[count])
    count = count + 1
