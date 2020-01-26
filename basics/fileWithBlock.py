#  no need to close file with this with

with open("file.txt") as f:
    print(f.read())




file = open("file.txt")

print(file.read())

file.close()


