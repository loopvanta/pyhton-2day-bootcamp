# f string
name=input("enter your name:")
print(f"good afternoon, {name} ")
# OR
name=input("enter your name:")
print("good afternoon",name)

letter = ''' Dear <|name|>,
You are selected!
<|date|>'''
print(letter.replace("<|name|>","komal").replace("<|date|>","22 july 2025"))

