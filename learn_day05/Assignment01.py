basic_pay = input("Enter Basic Pay of Employee")

if len(basic_pay) > 0 and basic_pay.isnumeric():
    basic_salary = int(basic_pay)
    hra = 0.1 * basic_salary
    ta = 0.05 * basic_salary
    total_pay = basic_salary + hra + ta
    professional_tax = 0.02 * total_pay
    net_pay = total_pay - professional_tax
    print("Net Salary after deduction is", net_pay)
else:
    print("Enter Valid Input for Basic Salary")