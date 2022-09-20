'''
try:
    risky code
except Error:
    handling error
finally:
    this block executes regardless of error or not
'''
list = [40, 10,20,30]
var_age = 20
print("This is before calling list")
try:
    print(list[1])
    div = var_age / list[0]
    print("Div ", div)
except (IndexError, ZeroDivisionError) as ie:
    print("Exception occurred :: ", ie)
finally:
    print("This block will execute if or not there is an error")