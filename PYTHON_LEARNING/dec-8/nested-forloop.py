"""
n=5
for i in range(n):
    for j in range(n):
        print("*",end="")  #end="" means don’t go to next line,So stars get printed side by side
    print()
"""

"""
for i in range(1,5):
    for j in range(i):
        print(i,end="")
    print()
"""


"""
for i in range(5,0):
    for j in range(i):
        print("*",end="")
    print()
"""
   


"""
for i in range(0, 8):   
    for j in range(i+1):
        print(j+1,end="")
    print()
"""


n=5
for i in range(n):
    for j in range(n - i):      # decreasing numbers
        print(j + 1, end="")
    print()
