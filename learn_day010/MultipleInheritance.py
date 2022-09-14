class Employee:

    def __init__(self, name, id):
        self.emp_id = id
        self.emap_name = name
        self.type = ""
        print("Employee Created with {} and ID is {}".format(self.emap_name, self.emp_id))

    def discount(self, type):
        self.type = type
        print("Employee is availing discount code ",self.type)

class Validation:
    def __init__(self, address):
        self.address = address
        self.type = "Area Code"
        print("Address is Validated ", self.address)

    def discount(self, type="Area Code"):
        self.type = type
        print("Validation:: Employee is availing {} discount ".format(self.type))


class Customer(Employee, Validation):

    def __init__(self, name, id, address):
        Employee.__init__(self, name, id)
        Validation.__init__(self, address)
        print("Customer is created")


    def discount(self, type="ONLINE"):
        Validation.discount(self, type)


# emp = Employee('Neil', 101)
cust = Customer('Neil', 101, '3375 Spring Hill Pwky')
cust.discount()