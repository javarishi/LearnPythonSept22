'''
while condition:
    block of code executes when condition is true
    condition modifier
'''

# Add 1 to 10 with while loop
counter = 0
total = 0
while counter <= 10:
    total = total + counter
    # counter = counter + 1
    counter += 1
print("Total ::", total, "Counter :: ", counter)

# Add all even numbers till 25
# add all odd numbers till 30