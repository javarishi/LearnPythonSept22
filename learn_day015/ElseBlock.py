'''
try:
    risky code
except Error:
    error handling
else:
    you cannot have else after finally
    executes only if try block completes without an error
finally:
    optional finally block
'''

list = [60, 10,20,30]
var_age = 20
print("This is before calling list")
try:
    print(list[1])
    div = var_age / list[0]
    print("Div ", div)
except (IndexError, ZeroDivisionError) as ie:
    print("Exception occurred :: ", ie)
else:
    print("This is executed when try completes without any errors")
finally:
    print("This block will execute if or not there is an error")