# Variables - value varies - alias name to it
# int
x = 10
x1 = 10
x2 = 10
x3 = 10
print(id(x), id(x1), id(x2), id(x3))
x1 = 11
print(id(x), id(x1), id(x2), id(x3))
# float
y = 10.9
# complex
z = 1 + 7j
# boolean
bool = False
# String
str_val = "You can give anything here"
# type - checks what python thinks about your variable
print(x, type(x), id(x))
print(y, type(y), id(y))
print(z, type(z), id(z))
print(bool, type(bool), id(bool))
print(str_val, type(str_val), id(str_val))
