k = ("komal", 89, 5, 5, "tia")
print(k.count(5))
print(k.index("komal"))
# print(max(k)) this will give a error because python does not know which int or str have the max value
print(len(k)) #provide the lenght of the tuple
#  to join two tuples wee use concatenate
t1 = ("komal",)
t2 = ("meshram",)
con = t1 + t2
print(con)
# if you want to repeat the tuple you can
t3 = (1, 2, 3 ,4)
repeat = t3 * 2 # here 2 means 2 time the tuple will repeat
print(repeat)
#  to check the value is in your tuple
print(2 in t3) #it will return a boolean value if the value is present true will return otherwise false



