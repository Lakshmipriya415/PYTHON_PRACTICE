marks=[40,42,41]

marks.append(43)

print(len(marks))
print(sum(marks))
print(sum(marks)/len(marks))
print(marks[3])
print(type(marks))
print(max(marks))
print(min(marks))


marks.insert(1 , 40.5)
print(marks)

marks.remove(43)
print(marks)

print(marks.index(42))   #it will the index number at that value 42

marks.reverse()
print(marks)


marks1=marks.copy()
print(marks1)


marks.clear()
print(marks)

marks.append(42)
print(marks)

marks.append(42)
print(marks)

print(marks.count(42))

marks.insert(1,45)
print(marks)

marks.sort()
print(marks)

marks.pop(1)
print(marks)

marks.extend([3,4])
print(marks)
