sampleDictionary = {
    "Model" : "Toyota",
    "Color" : "Grey",
    "Year" : 2010,
    "State" : "GA",
    "Plate" : "TXA678J",
}
# get
print(sampleDictionary["Model"])
print(sampleDictionary.get("Color"))
# add?
sampleDictionary["VIN"] = "320948309284JIJI4235"
print(sampleDictionary)
# update
sampleDictionary["State"] = "TN"
print(sampleDictionary)
# remove - with key
sampleDictionary.pop("Plate")
print(sampleDictionary)
# popitem
sampleDictionary.popitem() # remove last entered data in dictionary
print(sampleDictionary)

# Membership - in on dictionary is checking for key
if "Color" in sampleDictionary:
    print("Yes , Color is present")

if 'TN' in sampleDictionary.values():
    print("yes TN is present in values")

# Iteration - with key
for eachKey in sampleDictionary:
    print(eachKey, sampleDictionary.get(eachKey))

print("Getting Key and Value together - with item function")

for key, value in sampleDictionary.items():
    print(key, value)

print("Iteration of values")
for eachValue in sampleDictionary.values():
    print(eachValue)

print(len(sampleDictionary))

sampleDictionary.clear()
print(sampleDictionary)