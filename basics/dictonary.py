# dictionary is key value pair like map in java

di = {1: "jan", 2: "feb", 3: "nov", 4: {"sunday": 1}}

print(di)
print(di[1])
print(di[4])
del di[4]

print(di)

d2 = di.copy()

print(d2.keys())
print(d2.items())

d3 = dict()



