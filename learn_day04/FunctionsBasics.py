'''
def function_name(input parameters):
    indented block defines function body
    option return statement
    return output

calling a function:
function_name(input)
'''

def shout(text):
    str_text = str(text)
    if len(str_text) > 0:
        print(str_text.upper())
    else:
        print("Insufficient Data")

shout("Hello Now")
shout('')