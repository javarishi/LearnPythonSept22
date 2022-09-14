'''
Class is blueprint of object.
Class has properties and functions (methods)
if methods are declared without class - type is function
print(type(greet)) # <class 'function'>
if method is declared in class - type is method
print(type(hello.greet)) # <class 'method'>
'''

class HelloWorld:
    '''
    Default constructor provided by interpreter is empty
    Constructor / initializer will act as normal method
    '''
    def __init__(self, input_age=0.5):
        print("HelloWorld Init Method")
        self.message = "Hello Students! Welcome to Python OOPS"
        self.age = input_age

    '''
    functions in class are exactly same in rules as normal functions 
    except they have additional argument called self - instance of own class
    '''
    def greet(self, language):
        if len(language) > 0:
            print("Welcome ! in ", language, self.message)
        else:
            print("Just Welcome!")
    '''
        Static methods are attached to class and have no dependecy on self
        Static methods are declared with decorator - classmethod 
        cls - acts as first parameter representing class 
    '''
    @classmethod
    def tax_calculation(cls, bill_amount):
        tax_calc = bill_amount * 0.12
        print(bill_amount, tax_calc)
        return tax_calc


''' Creating object / instance of class '''
hello = HelloWorld(1.5) # hello is instance of class HelloWorld
hello2 = hello
hello2.greet("English")
print(type(hello2.greet)) # <class 'method'>
print(hello2.message, hello2.age) # . operator allow instances to access propertise and methods of class

helloAgain = HelloWorld(2.5)
helloAgain.message = "Hello Again! We mate earlier!"
helloAgain.greet('')
print(helloAgain.message)

HelloWorld.tax_calculation(100)
