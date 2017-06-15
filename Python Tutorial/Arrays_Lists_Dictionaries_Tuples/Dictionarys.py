dictionary1 = {1:'hi', 2:'hello', 'three':'hey', 4:24, 4.2:87}
# dictionaries are noted by curly brackets and they are mutuable (which means
# they can be changed after they're made

# dictionaries enbale developers to specify keys as well as values

print("The keys of dictionary1 are",dictionary1.keys())
print("The corresponding values of dictionary1 are",dictionary1.values())
print("\nThe value at key three of dictionary1 is: ",dictionary1['three'])

dictionary2 = dictionary1.copy() # copy dictionary1 into dictionary2
dictionary1.clear()
print("dictionary2 items after dictionary1 was copied:", dictionary2.items())
print("dictionary1 items after it was cleared:", dictionary1.items(),"\n")
                # dictionary.items gives dcitionary keys with their values

for item in dictionary2: # this will print all dictionary2 keys
    print(item)

dictionary3 = {6:77, 'two':"snack"}
dictionary2.update(dictionary3) # dictionary3 is joined to dictionary2
print("\ndictionary2 after dictionary3 joined it:")
print(dictionary2.items())

print("\nLength of dictionary2 is",len(dictionary2))
