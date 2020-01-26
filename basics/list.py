# collection of different values

batsman = ["sachin", "dhoni", "kohli"]
print(batsman)

print(batsman[2])  # accessing items using index

print(batsman[0]+batsman[1])

batsman[1] = "dravid"

print(batsman)

print(len(batsman))

batsman.append("dhoni")  # add at the end of the list

print(batsman)

batsman.insert(1, " rohit ")  # add at any index
print(batsman)

index = batsman.index("kohli")
print(index)

batsman.pop(3)  # remove the item from list

print(batsman)

players = batsman[0:2]  # creating the new list out of existing list  // slicing of the list
print(players)
print("*#"*20)

batsman.sort()
print(batsman)

print(batsman[::2])  # slicing



