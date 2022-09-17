# file = open('/RISHI/H2K/FileIO/demofile_write.txt', 'w')
file = open('/RISHI/H2K/FileIO/demofile_append.txt', 'a')
for i in range(0, 10):
    file.write("This is new Line {} \n".format(i))
print("Done!")
file.close()

filex = open('/RISHI/H2K/FileIO/demofile_x.txt', 'x')
filex.close()