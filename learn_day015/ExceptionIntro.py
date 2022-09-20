'''
try:
    risky code which might throw an error
except <OptionalError>:
    How do you want to handle this situation
except <OptionalError2>:
    How to handle other error
'''

list = [0, 10,20,30]
var_age = 20
print("This is before calling list")
try:
    print(list[1])
    div = var_age / list[0]
    print("Div ", div)
except IndexError as ie:
    print("Index is not given properly", ie)
except ZeroDivisionError as ze:
    print("Divided by 0 is Bad Math", ze)
print("This is after calling list")