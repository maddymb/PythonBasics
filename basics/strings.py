a = 'single quotes'

print(a)

b = "double quotes"

print(b)

b = "double \
quotes"

print(b)

print(b[:])  # print full string
print(b[2:4])  # print substring starts 2 to 4
print(b[-4])  # print will work like circle
print(len(a))  # length of the string

print(a[::-1])  # reverse of the strings
a = a[::-1]
print(a)
a = a[::-1]

fname = "madhur"
lastname = "bharadwaj"

print("my name is "+fname+lastname)
print("my name is %s %s" % (fname, lastname))  # &s works as a place holder


