#Python refers to values that cannot change as immutable, and an immutable list is called a tuple.
#A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.   
#Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#Negative Indexing
#Negative indexing means start from the end, -1 refers to the last item, -2 refers to the second last item etc.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#Range of Indexes
#You can specify a range of indexes by specifying where to start and where to end the range
#When specifying a range, the return value will be a new tuple with the specified items.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#By leaving out the start value, the range will start at the first item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#By leaving out the end value, the range will go on to the end of the list
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#Change Tuple Values
#Once a tuple is created, you cannot change its values. Tuples are unchangeable.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")   
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)    
#Add Items
#Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
#You can add items to a tuple by concatenating it with another tuple:
thistuple = ("apple", "banana", "cherry")
thistuple += ("orange",)    
print(thistuple)
#Note: When we create a tuple with only one item, we have to add a comma after the item, otherwise it will not be recognized as a tuple.
#This is because Python uses the comma to determine that it is a tuple, not the parentheses.
#Remove Items
#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
