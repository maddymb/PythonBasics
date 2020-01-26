li = ["madhur", "deepali", "nidhi", "maddy"]
list = [["madhur","hero"], ["deepali","sundar"], ["nidhi", "besti"], ["maddy", "supe"]]

di = dict(list)

print(li)
print(list)
print(di)

for item in li:
    print(item)


for item, type in list:
    print(item, type)


for item, type in di.items():
    print(item, type)






