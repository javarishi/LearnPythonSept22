'''
for eachVar in collection:
    block of code executed for eachVar in collection

range function - generate the iteration numbers
range (start, end, step)
start - inclusive 0 - 0 will be included
end - execluded - 10 - last number will 9
step --> last number + step
'''

total = 0
for eachNumber in range(0,25,2):
    print(eachNumber)
    total = total + eachNumber

print("total " , total)