"""
def display(n):
    if n == 0:   # base case (stop here)
        return
    print(n)
    display(n - 1)   # function calling itself

display(5)
"""




def fact(n):
    if n == 1:          # base case
        return 1
    factorial = n * fact(n - 1)   # recursive call
    return factorial

print(fact(5))

