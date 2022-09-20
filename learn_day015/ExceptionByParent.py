'''
- you can have any number of except blocks
- You should always except specific error
- Specific (Child Class) first, generic (Parent class) later
try
    risky set of codes
except Exception:
    all the subclasses of Exception will be handled
'''
list = [0, 10,20,30]
var_age = 20
print("This is before calling list")
try:
    print(list[1])
    div = var_age / list[0]
    print("Div ", div)
except IndexError as ie:
    print("IndexError occurred :: ", ie)
except Exception as ie:
    print("Exception occurred :: ", ie)

print("This is after calling list")