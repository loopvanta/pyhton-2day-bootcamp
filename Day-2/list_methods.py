friends = ["Apple", "orange", 5, 3.908, False, "Akash"]
# print(friends)
# print(friends.append("komal")) this will print none because append method have a reurn type as none
# we can add new values to the list at the end using append method

friends.append("komal")
print(friends)
# the right way to adda value to the list is above shown this will update your list 
l1 =[1, 34, 56, 62]
l1.sort() # this will sort the list in ascending order
print(l1)
l1.reverse()  # this will reverse the list
print(l1) 
l1.insert(3,"kartik") #this will insert the word kartik at the index 3
print(l1)
l1.pop(4) #this will delete a element of the index 4
print(l1)
# to know anyone's return value print(variabe.method(index))
# we can also see the return value like
value = l1.pop(3)
print(value)
l1.remove(34) #this removes the value if no value is passed it will pass a valuerror
print(l1)

