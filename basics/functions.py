# built in function

a = 4
b = 6
c = sum((a, b))

print(c)

# user define

def func():
    print("hello")


func()

def fun(a,b):
    """This is doc string"""
    print("Sum", a+b)
    return a+b

fun(4,7)

print(fun(4,6))

print(fun.__doc__)