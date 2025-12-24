numbers=[1,2,3,4,2,1]
print(numbers)

numbers_set=set(numbers)
print(numbers_set)

numbers_set.add(4)
numbers_set.add(0)
print(numbers_set)

print(max(numbers_set))
print(len(numbers_set))
print(sum(numbers_set))
numbers_set.remove(4)
print(numbers_set)
print( 1 in numbers_set)


"""
In a set we can perform union, intersection, difference operations
union check by ->  | operator   (combine both set elements)
Intersection check by ->  & operator (elements both in a and b sets)
difference check by ->  - operator  (elemnts prsent in a not in b is difference)
symmetric difference ->  Elements that are in either set, but NOT in both. formula A ^ B = (A - B) ∪ (B - A)

"""
numbers_1_to_6_set1=set(range(1,6))
print(numbers_1_to_6_set1)

numbers_4_to_11_set2=set(range(4,11))
print(numbers_4_to_11_set2)


print(numbers_1_to_6_set1 | numbers_4_to_11_set2)
print(numbers_1_to_6_set1 & numbers_4_to_11_set2)
print(numbers_1_to_6_set1 - numbers_4_to_11_set2)   # A-B
print(numbers_4_to_11_set2 - numbers_1_to_6_set1)   # B-A
