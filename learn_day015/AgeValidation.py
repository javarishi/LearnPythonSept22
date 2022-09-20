from learn_day015.BusinessErrors import AgeValidationError

def age_validation():
    try:
        age = input("Enter customer age:")
        int_age = int(age)
        if int_age > 18:
            return "Alcohol Purchase is Allowed"
        else:
            raise AgeValidationError("Age is under 18")
    except ValueError as ve:
        print("Wrong age Entered")

try:
    message = age_validation()
    print(message)
except AgeValidationError as ae:
    print(ae)