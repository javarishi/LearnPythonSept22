'''
Modes
File Modes:
r = read only - you cannot change the file - gives error if file doesnt exists
w = write mode - write new content every time - to create the file when not exists
a = append mode - append the content to existing one - to create the file when not exists
x = create - just create = error if exists - to create the file when not exists
file formats:
t = text
b = binary
'''
# by default file open uses - rt
file = open('/RISHI/H2K/FileIO/demofile.txt')
'''
print(file.read(10))
print(file.read(15))
print(file.read())

for eachLine in file:
    print("Processing : " , eachLine)
'''
with open('/RISHI/H2K/FileIO/demofile.txt', "rt") as file1:
    for eachLine in file1:
        print(eachLine)