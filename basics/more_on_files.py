file = open("file.txt")
print(file.tell())  # will tell file pointer location
print(file.readline())
print(file.tell())
print(file.readline())
print(file.tell())

file.seek(10)  # reset the pointer as per your wish

print(file.readlines())

file.close()