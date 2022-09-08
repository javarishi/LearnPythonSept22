# normal variables first, dynamic parameters later
def students_data(cls_name, subj_name, *args):
    print(cls_name, subj_name)
    for eachStudent in args:
        print("Processing ...", eachStudent)

def student_details(name, roll_name, **kwargs):
    print(name, roll_name)
    print(kwargs, type(kwargs))
    for key, value in kwargs.items():
        print(key, value)

def sample_function(normal_variable, *args, **kwargs):
    print(normal_variable)
    print(args)
    print(kwargs)

''' 
Order of argument declaration will be
1. Normal Argument
2. args - dynamic argument
3. kwargs - dynamic keyed Argument
'''

students_data("Third Year", "Python" , 101, 102, 103, 104, 105, 106)
student_details("David", "101", address="XYZ Lane", major="programming", minor="Cloud computing", cgpa=8.98)