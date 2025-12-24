numbers= dict(a=5,b=6,c=8, d=9)
print(type(numbers))
print(numbers)

########### Access and Modify Values
numbers['d']=10
print(numbers)
print(numbers['a'])


########## Handling non existing keys
#print(numbers['e'])

#To avoid use get() method, provide a default value if needed
print(numbers.get('e',10))


########## Explorint dictionary methods
print(numbers.keys())
print(numbers.values())
print(numbers.items())


########## Iterating a dictionary 
for key,value in numbers.items():
    print(f"{key} {value}")


########## DEL a dictionary
numbers['a']=0
del numbers['a']
print(numbers)

