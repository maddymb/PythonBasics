#FILE IO Basics
"""
"r" - Open file for reading - default
"w" -  Open file for writing
"x" - Create file if not exists
"a" - Add more content to a file
"t" - text mode - default
"b" - binary mode
"+" - read and write mode
"""


file = open("file.txt", "r")

# content = file.read()
# print(content)
#
# readLine = file.read(2)
# print(readLine)
#
# for line in file:
#     print(line)
#
# for li in content:
#     print(li)

# print(file.readline())
# print(file.readline())
# print(file.readline())


print(file.readlines())





file.close()

