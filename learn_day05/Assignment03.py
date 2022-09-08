N = int(input("How many numbers you want to enter"))
number_list = []
for eachNumber in range(0, N):
    new_number=int(input("Enter number:"))
    number_list.append(new_number)

max = number_list[0]
min = number_list[0]
total = 0
for eachNumber in number_list:
    if max < eachNumber:
        max = eachNumber
    if min > eachNumber:
        min = eachNumber
    total = total+eachNumber

print("Max ", max)
print("Min", min)
print("Total", total)
print("Average", total / len(number_list))