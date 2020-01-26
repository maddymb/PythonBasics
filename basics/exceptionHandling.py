# try and except

num1 = 5
num2 = 0

try:
    print(num1/num2)

except Exception as e:
    print("division by zero is not allowed")
    print(e)