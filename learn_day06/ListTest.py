# Lists are written with square brackets.
sampleList = [89,12,67,13,14,"Rishi", 67.78]
# Access Items: sampleList[1] - Sublist with N:N
print(sampleList[4:7])
# Add Element: sampleList.append("newItem")
sampleList.append("newItem")
print(sampleList)
sampleList.insert(3, 15) # this will move existing data to next position
print(sampleList)
sampleList.remove("Rishi")
print(sampleList)
sampleList.pop(-1)
print(sampleList)
# membership - exists in list or not - in
if 67 in sampleList:
    print("67 is in")
if 88 not in sampleList:
    print("88 not in")

sampleList.pop(-1)
sampleList.sort() # sorting changes existing indexes
print(sampleList)
sampleList.reverse()
print(sampleList)
print(len(sampleList))
# for loop
for eachItem in sampleList:
    print(eachItem)

# clear entire list
sampleList.clear()
# del sampleList
print(sampleList)