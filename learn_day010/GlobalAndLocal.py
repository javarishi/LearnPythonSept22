# global variable - all methods look this value
message = "Hello"

def greet():
    global message
    message = "Hola!" # Local Variable - carrying local value - expires with function
    print("Inside Function Greet: " , message)

print("Before function call : " , message)
greet()
print("After function call : " , message)  