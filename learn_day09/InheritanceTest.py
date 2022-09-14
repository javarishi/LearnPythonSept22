class Customer:
    def __init__(self, name, age, doctor_name):
        self.name = name
        self.age = age
        self.doctor_name = doctor_name
        print("Customer is created ", self.name, self.age)

    def prescibtion(self):
        print("Paitient of Dr", self.doctor_name , " name ", self.name )

# Class PreferredCustomer is a Customer - IS A test is for checking inheritance
class PreferredCustomer(Customer):
    def __init__(self, name, age, doctor_name, email):
        Customer.__init__(self, name, age, doctor_name)
        self.email = email
        print("PreferredCustomer is created - with email id :: ", self.email)

    def send_offer(self):
        print("Offer is sent to ", self.name, " on his email ", self.email)

    def discount(self):
        print("PreferredCustomer offers {} % discount ".format(0.5))

class CreditCardCustomer(PreferredCustomer):
    # Chaining Constructor - where Super class Constructor called as First Statement of Child Class Constructor
    def __init__(self, name, age, doctor_name, email, address, ssn):
        PreferredCustomer.__init__(self, name, age, doctor_name, email)
        self.address = address
        self.ssn = ssn
        print("Credit Card Issued for Customer ", self.name , "and sent to ", self.address)

    def discount(self):
        #  If the methods is exactly same as in Parent, the method hides the implementation from Parent - this concept is called as Overriding
        print("Additional 1% discount to ", self.email)

# pCust01 = PreferredCustomer('Rishi', 37, 'Raghvan')
ccCust01 = CreditCardCustomer('Rishi', 37, 'Raghvan', "rishi.h2kinfosys@gmail.com", "3374 Spring Hill Pkwy, Smyrna 30080", "30294392084")
ccCust01.prescibtion()
ccCust01.send_offer()
ccCust01.discount()