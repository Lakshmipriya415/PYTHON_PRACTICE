"""
for i in range(2,20,-1):
	print(i)
"""



"""
sum=1
for i in range(1,11):
    sum=sum*i
    print(sum)
"""


"""
for i in range(1,11):
    print(f"5*{i}={5*i}")     #f-strings                                                                                                                                                            
    print(f"The value of is is {i}") 
x=5
y=3
print(f"the value of {x} and {y} is {x+y}")
multiple =5*3
print(multiple)
"""



"""
print(f"Value is {{5}}")
"""




"""
factorial=1
for i in range(1,7):
    factorial=factorial*i
print(factorial)
"""



"""
numbers=[1,2,3,4,5]    
largest= numbers[0]
for i in numbers:
    if i > largest:
        largest = i
print(largest)
"""



"""for i in range(0,-22,-2):   #print eben negative numbers
    print(i)
    """




def is_prime(number):
    
    if number<2:
        return False
    
    for divisor in range(2, number):
        if number%divisor==0:
            return False
    return True
    
print(is_prime(5))
