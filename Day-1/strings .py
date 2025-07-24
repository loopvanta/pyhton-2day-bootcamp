# we can use single,double,triple quotes
# strings are immutable which mean it cannot change once it made
# to find the length of name
name = "komal"
print(len(name))
# or
name = "meshram"
k=len(name)
print(k)
# index in the string starts from the 0 to (length-1) in python,in order to slice a string ,we use the following syntax
# sl = name[ind_start:ind_end]
nameshort = name[0:3]
print(nameshort) #it will include till 2 no. of index value
# we can use minus indexes also it starts from back of the length from -1 to till where the lenght of the string goes
# if we have to print only the one character of the string
charr1 = name[3]
print(charr1)

# slicing with ski values
word = "amazing"
print(word[1:6:2]) #first it will take the letters from index 1 to 6 which are mazin then it will sselect letters as per gapping 2 words
# output will be "mzn"

