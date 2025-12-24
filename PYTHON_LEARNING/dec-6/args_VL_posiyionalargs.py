"""
def add(*args):
    addall = 0
    for num in args:
        addall += num
    print(addall)

add(1, 2, 3)
"""


def multiply(*args):
    mul=1
    sum=0
    for i in args:
        mul=mul*i
        print(mul)
        print("1111")
        sum=sum+mul
        print(sum)
        print("2222")

multiply(1,2,3)
