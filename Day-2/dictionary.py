# dictionary is a  key-value pair
marks = {
    "komal" : 100,
    "laya" : 99,
    "dia" : 97,
    0 : "harsh"
}
print(marks, type(marks))
# to print the corresponding marks of the of the student
print(marks["komal"])
# in python the concept of dictionary case because it look ups faster in O(1); if we have 1000 student of marks so to find the marks of one person dict makes it super easy
# it is unorderd
# it is mutable
# it is indexed  which means that it does not find the value one by one it directley searches the given corresponding value
# cannot contain duplicate keys
