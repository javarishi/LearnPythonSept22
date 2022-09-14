# argument - i/p- parameter - variable
# default parameter values (Keyed argument)
# keyed parameters are always last
def greet(name, message="How are you?"):
    print("Hello ", name, message)

def address(addressLine1, addressLine2, county, city, state, zipcode):
    print(addressLine1)
    print(addressLine2)
    print(city, county)
    print(state, zipcode)

def square(num):
    return num*num

def all_basic_math(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    division = num1 / num2
    multiplication = num1 * num2
    return addition, subtraction, division, multiplication

# Input parameters may not required order if name of variable is specified (all the names)
address(county="Smyrna",
        addressLine1= "3375 Paces Ferry Road",
        addressLine2="Georgia Lane",
        city="Atlanta",
        state="GA",
        zipcode="33639")

five_sqr = square(5)
print(five_sqr)
greet("Rishi", "Howdy")
greet("Students")
return_cal = all_basic_math(10,2)
print(return_cal, type(return_cal))
addition = return_cal[0]
print(type(greet)) # <class 'function'>