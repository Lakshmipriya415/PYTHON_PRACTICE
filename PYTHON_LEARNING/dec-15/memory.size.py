import sys
x_int = 123
x_float = 123.45
x_str = "Hello"
x_list = [1, 2, 3, 4, 5]

print("Integer size:", sys.getsizeof(x_int), "bytes")
print("Float size:", sys.getsizeof(x_float), "bytes")
print("String size:", sys.getsizeof(x_str), "bytes")
print("List size:", sys.getsizeof(x_list), "bytes")

