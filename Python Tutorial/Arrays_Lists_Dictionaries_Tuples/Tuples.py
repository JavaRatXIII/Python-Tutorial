tuple1 = ("apples", 3, 7, 9.2, "wind") # tuples are noted by normal brackets

# tuples are immutable objects which means it cannot be changed after it has 
# been made, to change a tuple you will have to create a new table with the new
# added or removed values

for item in tuple1:
    print(item)

print("\nLength of tuple1 is", len(tuple1),"\n")

tuple2 = tuple1 + (786,) # add 786 to tuple1 inside of a new tuple, tuple2
for item in tuple2:
    print(item)

print("\n")
list1 = [1, 2, "hi", 6.2]
tuple3 = tuple(list1) # converts list1 into a tuple
count = 0
for item in tuple3:
    print("tuple item", count, ":", item)
    count = count + 1

tuple4 = (24, 6, 7, 32, 78, 85, 4, 29, 39, 87)
print("\nMax value in tuple4 is", max(tuple4),"Minimum value is", min(tuple4))
