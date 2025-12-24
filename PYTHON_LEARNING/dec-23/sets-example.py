s1= {1,2,3,4}
s2= {4,5,6,7}
result=s1.union(s2)   #same as s1 | s2
print(result)


list_of_set1= [set([1,2]),set([3,4]),set([5,6])]
list_of_set2= [set([5,6]),set([7,8])]
union_result=set.union(*list_of_set1,*list_of_set2)
print(union_result)


numbers=[1,2,3,4,5,6,7,8,9,10]
res= {x**2 for x in numbers if x%2==0}    #This is a set comprehension.
print(res)
