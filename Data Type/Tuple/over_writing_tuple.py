#Over writing a Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
print("\n\t----$$$$$----\t\n")
#Once a tuple is created, you cannot change its values. Tuples are unchangeable.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")   
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)
