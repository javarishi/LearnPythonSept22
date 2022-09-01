message = "Hello {}, this is {}!".format("Rishi", "interesting")


# Python String is array of characters
print(message)
print(message[0])
print(message[0:5]) # string[start:end+1] - start is included and end is excluded
print(message[-1]) # access from tail
print(len(message))

message = "Hello {}, this is {}!".format("Students", "Educational")
print(message)
# data conversion
print("message.upper() :: ", message.upper())
print("message.lower() :: ", message.lower())
print("message.isupper() :: ", message.isupper())
print("message.islower() :: ", message.islower())
print("message.title() :: ", message.title())
print("message.capitalize() :: ", message.capitalize())

# find
print("message.find('e') :: ", message.find("e"))
print("message.count('e') :: ", message.count('e'))

# search - find to give positive result
print("message.find('rishi') :: ", message.find("rishi"))

age = "100000"
print(" age.isalnum() :: ", age.isalnum())
print(" age.isdigit() :: ", age.isdigit())

name = "rishi"
print(" age.isalpha() :: ", age.isalpha())
print(" name.isalpha() :: ", name.isalpha())

