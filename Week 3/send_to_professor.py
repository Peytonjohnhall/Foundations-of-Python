"""
TRY THIS: LIST SLICES AND INDEXES 
Using what you know about the len () function and list slices, 
how would you combine the two to get the second half of a list 
when you don't know what size it is? 
Experiment in the Python shell to confirm that your solution works.
Example: myList = [1,2,3,4,5,6,7,8,9,0,11,12,13,14]
Answer (8,9,0,11,12,13,14]
"""

myList = [1,2,3,4,5,6,7,8,9,0,11,12,13,14]

myList = [1,2,3,4,5,6,7,8,9,0,11,12,13,14]
# we need the second half of the list but do not know the length of it
starting_index = len(myList) // 2 # integer division needed as these are not floats
myList[starting_index:]

# let's try with floats
myList = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,0.0,11.0,12.0,13.0,14.0]
starting_index = len(myList) / 2
myList[starting_index:]

# try with strings?
myList = ["one", "two", "apple", "dog", "cat" "eight", "seven", "twelve", "zero"]
starting_index = len(myList) / 2
myList[starting_index:]
