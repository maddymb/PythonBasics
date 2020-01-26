file = open("file.txt", "w")  # write mode

file.write("I am hero")
file.close()


file = open("file.txt")
content = file.read()
print(content)
file.close()


file = open("file.txt", "a")  # append mode
a = file.write("madhur")
print(a)
file.close()

file = open("file.txt")
content = file.read()
print(content)
file.close()


# handle read and write both


file = open("file.txt", "r+")
print(file.read())

file.write("thanks")
file.close()
file = open("file.txt", "r+")
print(file.read())

file.close()
















