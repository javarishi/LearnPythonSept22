'''
In walgreens store - take an age of customer and allow alcohol purchase only if customer age
is greater than 18 otherwise not allowed
'''

input_age = input("Enter Customer Age:")
if input_age.isnumeric():
    age = int(input_age)
    if age > 18:
        print("Alcohol Purchase is allowed")
    else:
        print("Alcohol Purchase is NOT allowed")
else:
    print("Invalid Input Provided")