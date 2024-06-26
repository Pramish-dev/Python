# Python -Add List Items

# APPEND ITEMS
"""
 To add an item to the end of the list, use the 'append()' method:

 Example:
 Using the append() method to append an item:
 """
thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

#OUTPUT: ['apple', 'banana', 'cherry', 'orange']

# INSERT ITEMS
"""
To insert a list item at a spcified index, use the insert() method.

The 'insert()' method inserts an item at the specified index:
"""
thislist=["apple","banana","cherry"]
thislist.insert(1,"orange")
print(thislist)
# OUTPUT: ['apple', 'orange', 'banana', 'cherry']

#EXTEND LIST
# To append elements from another list to the current list, use the 'extend()' method.

#Example: Add the elements of tropical to thislist:

thislist= ["apple","banana","cherry"]
tropical= ["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)

# OUTPUT: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Add Any Iterable
# To 'extend()' method does not have to append lists, you can add any iterable object(tuples,sets,dictionary etc.)

# Add elements of a tuple to a list:
thislist = ["apple","banana","cherry"]
thistuple= ("kiwi","orange")
thislist.extend(thistuple)
print(thislist)

# OUTPUT : ['apple', 'banana', 'cherry', 'kiwi', 'orange']












