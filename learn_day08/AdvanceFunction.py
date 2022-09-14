'''
    Python respects functions / methods as first class members
'''

def shout(text):
    print(str(text).upper())

def calculator(action, num1, num2):
    def addition():
        sum = num1 + num2
        return sum

    def subtraction():
        sub = num1 - num2
        return sub

    if action == 'addition':
        return addition
    else:
        return subtraction

method_name = calculator('addition', 10, 10)
total = method_name()
print(total)

shout("Cheers!")
print("shout" ,type(shout))

rishiz_shout = shout
print("rishiz_shout" ,type(rishiz_shout))
rishiz_shout("Rishi shouting")